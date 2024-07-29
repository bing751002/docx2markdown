from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# 使用中文 BERT 模型
chinese_model = SentenceTransformer('distiluse-base-multilingual-cased-v1')
kw_model = KeyBERT(model=chinese_model)

doc = "自然語言處理是人工智能的一個重要分支,它致力於讓計算機理解和生成人類語言。"
custom_candidates = ["自然語言處理", "人工智能", "機器學習", "深度學習", "語言模型"]

keywords = kw_model.extract_keywords(doc, candidates=custom_candidates, top_n=3)
print(keywords)

