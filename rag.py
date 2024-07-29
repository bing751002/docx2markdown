import streamlit as st
import os
import sqlite3
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# 初始化資料庫
def init_db():
    conn = sqlite3.connect('rag_systems.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rag_systems
                 (name TEXT PRIMARY KEY, model TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS uploaded_files
                 (rag_name TEXT, filename TEXT, PRIMARY KEY (rag_name, filename))''')
    conn.commit()
    return conn

# 保存RAG系統到資料庫
def save_rag_system(conn, name, model):
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO rag_systems (name, model) VALUES (?, ?)", (name, model))
    conn.commit()

# 獲取所有RAG系統
def get_rag_systems(conn):
    c = conn.cursor()
    c.execute("SELECT name, model FROM rag_systems")
    return c.fetchall()

# 保存上傳的文件信息
def save_uploaded_file(conn, rag_name, filename):
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO uploaded_files (rag_name, filename) VALUES (?, ?)", (rag_name, filename))
    conn.commit()

# 獲取已上傳的文件
def get_uploaded_files(conn, rag_name):
    c = conn.cursor()
    c.execute("SELECT filename FROM uploaded_files WHERE rag_name = ?", (rag_name,))
    return [row[0] for row in c.fetchall()]

# 初始化向量存儲
def init_vector_store(texts, collection_name):
    embeddings = HuggingFaceEmbeddings()
    return Chroma.from_texts(texts, embeddings, collection_name=collection_name)

# 初始化語言模型
def init_llm(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return HuggingFacePipeline(pipeline=pipe)

# 處理上傳的文件
def process_file(file, rag_name):
    text = file.getvalue().decode("utf-8")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(text)
    return init_vector_store(texts, rag_name)

def main():
    st.title("多RAG系統聊天GPT")

    # 初始化資料庫連接
    conn = init_db()

    # 初始化會話狀態
    if 'rag_systems' not in st.session_state:
        st.session_state.rag_systems = {name: None for name, _ in get_rag_systems(conn)}
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_rag' not in st.session_state:
        st.session_state.current_rag = None

    # 側邊欄：RAG系統管理
    with st.sidebar:
        st.header("RAG系統管理")
        
        # 創建新的RAG系統
        with st.expander("創建新RAG系統"):
            new_rag_name = st.text_input("輸入新RAG系統名稱:")
            new_rag_model = st.selectbox("選擇模型", ["gpt2", "facebook/opt-350m"], key="new_model")
            if st.button("創建RAG系統") and new_rag_name:
                save_rag_system(conn, new_rag_name, new_rag_model)
                st.session_state.rag_systems[new_rag_name] = None
                st.success(f"已創建RAG系統: {new_rag_name}")

        # 選擇RAG系統
        rag_systems = get_rag_systems(conn)
        rag_name = st.selectbox("選擇RAG系統", [name for name, _ in rag_systems])
        if rag_name:
            st.session_state.current_rag = rag_name
            rag_model = next(model for name, model in rag_systems if name == rag_name)
            st.info(f"{rag_name} 使用的模型: {rag_model}")

        # 文件上傳
        if st.session_state.current_rag:
            with st.expander("上傳文件"):
                uploaded_file = st.file_uploader(f"上傳文件到 {st.session_state.current_rag}", type=["txt"])
                if uploaded_file:
                    try:
                        vector_store = process_file(uploaded_file, st.session_state.current_rag)
                        st.session_state.rag_systems[st.session_state.current_rag] = vector_store
                        save_uploaded_file(conn, st.session_state.current_rag, uploaded_file.name)
                        st.success(f"文件 {uploaded_file.name} 已上傳並處理")
                    except Exception as e:
                        st.error(f"處理文件時發生錯誤: {str(e)}")

            # 顯示已上傳的文件
            uploaded_files = get_uploaded_files(conn, st.session_state.current_rag)
            if uploaded_files:
                st.subheader("已上傳的文件:")
                for file in uploaded_files:
                    st.write(f"- {file}")
            else:
                st.info("尚未上傳任何文件")

    # 主界面：對話
    if st.session_state.current_rag:
        st.header(f"與 {st.session_state.current_rag} 對話")
        
        if st.session_state.rag_systems[st.session_state.current_rag] is not None:
            try:
                # 初始化對話檢索鏈
                rag_model = next(model for name, model in rag_systems if name == st.session_state.current_rag)
                llm = init_llm(rag_model)
                qa_chain = ConversationalRetrievalChain.from_llm(
                    llm, 
                    st.session_state.rag_systems[st.session_state.current_rag].as_retriever(),
                    return_source_documents=True
                )

                # 顯示對話歷史
                for human, ai in st.session_state.chat_history:
                    st.markdown(f"**Human:** {human}")
                    st.markdown(f"**AI:** {ai}")

                # 用戶輸入
                user_input = st.text_input("輸入您的問題:", key="user_input")
                if st.button("發送"):
                    if user_input:
                        with st.spinner("AI正在思考..."):
                            result = qa_chain({"question": user_input, "chat_history": st.session_state.chat_history})
                            response = result['answer']
                            st.session_state.chat_history.append((user_input, response))
                            st.experimental_rerun()

                # 清除對話按鈕
                if st.button("清除對話歷史"):
                    st.session_state.chat_history = []
                    st.experimental_rerun()
            except Exception as e:
                st.error(f"初始化對話系統時發生錯誤: {str(e)}")
        else:
            st.warning("請先上傳文件到此RAG系統")
    else:
        st.info("請在側邊欄選擇或創建一個RAG系統")

    # 調試信息
    st.sidebar.subheader("調試信息")
    st.sidebar.write("當前RAG系統:", st.session_state.current_rag)
    st.sidebar.write("RAG系統狀態:", {k: "已初始化" if v is not None else "未初始化" for k, v in st.session_state.rag_systems.items()})

if __name__ == "__main__":
    main()