import jieba
from transformers import BertTokenizer, BertModel
import torch

class ChineseNLP:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
        self.model = BertModel.from_pretrained("bert-base-chinese")

    def tokenize(self, text):
        return list(jieba.cut(text))

    def get_embedding(self, text):
        tokens = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**tokens)
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()