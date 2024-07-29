from docx_converter import DocxConverter
from chunking import Chunker
from chinese_nlp import ChineseNLP
from rag_system import RAGSystem
from topic_modeling import TopicModeler

def main():
    # 轉換docx為markdown
    converter = DocxConverter()
    markdown_path = converter.convert_to_markdown("input.docx")
    print(f"Markdown file saved at: {markdown_path}")
    # 讀取markdown內容
    with open(markdown_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # 創建不同的chunks
    paragraph_chunks = Chunker.paragraph(markdown_content)

    # 初始化NLP工具
    nlp = ChineseNLP()

    # 為每個chunk創建嵌入
    embeddings = [nlp.get_embedding(" ".join(nlp.tokenize(chunk))) for chunk in paragraph_chunks]

    # 創建RAG系統
    rag = RAGSystem(embeddings, paragraph_chunks)

    # 示例查詢
    query = "你的問題"
    answer = rag.answer_query(query, nlp)
    print(f"Query: {query}")
    print(f"Answer: {answer}")

    # 生成meta信息和標籤
    meta_info, tags = TopicModeler.generate_meta_and_tags(markdown_content)
    print("Meta info:", meta_info)
    print("Tags:", tags)

if __name__ == "__main__":
    main()