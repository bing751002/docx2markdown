from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
import jieba

class TopicModeler:
    @staticmethod
    def preprocess_text(text):
        tokens = jieba.cut(text)
        return [token for token in tokens if token not in STOPWORDS and len(token) > 1]

    @staticmethod
    def generate_meta_and_tags(markdown_text, num_topics=5):
        processed_text = TopicModeler.preprocess_text(markdown_text)
        
        dictionary = corpora.Dictionary([processed_text])
        corpus = [dictionary.doc2bow(processed_text)]

        lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)

        topic_distribution = lda_model.get_document_topics(corpus[0])

        meta = {f"topic_{i}": weight for i, weight in topic_distribution}
        tags = [f"topic_{i}" for i, _ in sorted(topic_distribution, key=lambda x: x[1], reverse=True)[:3]]

        return meta, tags