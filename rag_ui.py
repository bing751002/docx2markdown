import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE

# 生成假數據
def generate_fake_data(query):
    documents = [
        "人工智能正在改變我們的生活方式。",
        "機器學習是人工智能的一個重要分支。",
        "深度學習在圖像識別領域取得了巨大突破。",
        "自然語言處理使機器能夠理解人類語言。",
        "強化學習在游戲AI中表現出色。"
    ]
    embeddings = np.random.rand(len(documents) + 1, 50)  # +1 for query
    similarities = cosine_similarity([embeddings[0]], embeddings[1:])[0]
    return documents, embeddings, similarities

st.set_page_config(layout="wide")
st.title('RAG查詢可視化模擬')

col1, col2 = st.columns([3, 2])

with col2:
    query = st.text_input('輸入您的查詢:', value="什麼是人工智能？")

    if query:
        documents, embeddings, similarities = generate_fake_data(query)
        
        st.subheader('檢索結果:')
        for i, (doc, similarity) in enumerate(zip(documents, similarities)):
            st.write(f"文檔 {i+1} (相似度: {similarity:.4f}):")
            st.write(doc)
            st.write('---')

with col1:
    if query:
        # 相似度條形圖
        fig = px.bar(
            x=[f"文檔 {i+1}" for i in range(len(documents))],
            y=similarities,
            labels={'x': '檢索文檔', 'y': '相似度'},
            title='查詢與檢索文檔的相似度'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # 相似度熱圖
        similarity_matrix = cosine_similarity(embeddings)
        fig = px.imshow(
            similarity_matrix,
            labels=dict(x="文檔", y="文檔", color="相似度"),
            x=['查詢'] + [f'文檔 {i+1}' for i in range(len(documents))],
            y=['查詢'] + [f'文檔 {i+1}' for i in range(len(documents))],
            title='查詢與檢索文檔的相似度矩陣'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # t-SNE可視化
        if len(embeddings) > 2:  # 確保有足夠的樣本進行t-SNE
            tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(embeddings) - 1))
            embeddings_2d = tsne.fit_transform(embeddings)
            
            df = pd.DataFrame({
                'x': embeddings_2d[:, 0],
                'y': embeddings_2d[:, 1],
                'label': ['查詢'] + [f'文檔 {i+1}' for i in range(len(documents))]
            })
            
            fig = px.scatter(
                df, x='x', y='y', text='label', color='label',
                title='查詢與檢索文檔的t-SNE可視化'
            )
            fig.update_traces(textposition='top center')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("樣本數量不足以進行t-SNE可視化")