import numpy as np
import faiss

class RAGSystem:
    def __init__(self, embeddings, texts):
        self.texts = texts
        self.dimension = len(embeddings[0])
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(np.array(embeddings))

    def retrieve_relevant_chunks(self, query_embedding, k=5):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [self.texts[i] for i in indices[0]]

    def answer_query(self, query, nlp):
        query_tokens = nlp.tokenize(query)
        query_embedding = nlp.get_embedding(" ".join(query_tokens))
        relevant_chunks = self.retrieve_relevant_chunks(query_embedding)
        
        # 這裡可以實現根據相關文檔塊生成答案的邏輯
        # 例如,可以使用語言模型來生成答案
        # 這裡只是一個簡單的示例
        answer = f"Based on the relevant information: {' '.join(relevant_chunks[:2])}"
        return answer