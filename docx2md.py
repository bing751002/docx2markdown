import os
import json
from docx import Document
import markdown
import jieba
from sentence_transformers import SentenceTransformer
import re
from bs4 import BeautifulSoup
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
from PIL import Image
import io

def docx_to_structured_markdown(docx_path, output_dir):
    doc = Document(docx_path)
    structured_content = []
    image_count = 0
    table_count = 0
    
    for element in doc.element.body:
        if element.tag.endswith('p'):
            style = element.style.name if element.style else 'Normal'
            content = {
                'type': 'paragraph',
                'style': style,
                'content': element.text
            }
            structured_content.append(content)
        elif element.tag.endswith('tbl'):
            table_count += 1
            table_filename = f"table_{table_count}.md"
            table_content = []
            for row in element.rows:
                row_content = [cell.text for cell in row.cells]
                table_content.append(row_content)
            
            # 将表格内容保存为Markdown
            with open(os.path.join(output_dir, table_filename), 'w', encoding='utf-8') as f:
                for row in table_content:
                    f.write('| ' + ' | '.join(row) + ' |\n')
                    if table_content.index(row) == 0:
                        f.write('| ' + ' | '.join(['---'] * len(row)) + ' |\n')
            
            content = {
                'type': 'table',
                'filename': table_filename,
                'caption': f"Table {table_count}"
            }
            structured_content.append(content)
        elif element.tag.endswith('pict'):
            image_count += 1
            image_filename = f"image_{image_count}.png"
            
            # 提取并保存图片
            image_element = element.find('.//v:imagedata')
            if image_element is not None:
                image_rel_id = image_element.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                image_part = doc.part.related_parts[image_rel_id]
                image = Image.open(io.BytesIO(image_part.blob))
                image.save(os.path.join(output_dir, image_filename))
            
            content = {
                'type': 'image',
                'filename': image_filename,
                'caption': f"Image {image_count}"
            }
            structured_content.append(content)
    
    return structured_content

def generate_markdown(structured_content, output_dir):
    markdown_content = ""
    for item in structured_content:
        if item['type'] == 'paragraph':
            markdown_content += f"<div class='{item['style']}'>\n\n{item['content']}\n\n</div>\n\n"
        elif item['type'] == 'table':
            markdown_content += f"<div class='table'>\n\n[{item['caption']}]({item['filename']})\n\n</div>\n\n"
        elif item['type'] == 'image':
            markdown_content += f"<div class='image'>\n\n![{item['caption']}]({item['filename']})\n\n</div>\n\n"
    
    with open(os.path.join(output_dir, "content.md"), "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    return markdown_content

def chunk_text(markdown_content, strategy="paragraph"):
    soup = BeautifulSoup(markdown_content, 'html.parser')
    if strategy == "paragraph":
        return [div.text for div in soup.find_all('div')]
    elif strategy == "sentence":
        text = soup.get_text()
        return re.split(r'(?<=[。！？])\s*', text)
    elif strategy == "fixed_length":
        text = soup.get_text()
        chunk_size = 500  # 可以根据需要调整
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def tokenize_chinese(text):
    return list(jieba.cut(text))

def embed_text(text, model):
    return model.encode(text)

def apply_lda(chunks, num_topics=5):
    tokenized_chunks = [tokenize_chinese(chunk) for chunk in chunks]
    tokenized_chunks = [[word for word in chunk if word not in STOPWORDS and re.match(r'\w+', word)] for chunk in tokenized_chunks]
    
    dictionary = corpora.Dictionary(tokenized_chunks)
    corpus = [dictionary.doc2bow(text) for text in tokenized_chunks]
    
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, 
                         random_state=100, update_every=1, chunksize=100, 
                         passes=10, alpha='auto', per_word_topics=True)
    
    return lda_model, dictionary

def generate_metadata(lda_model, dictionary, chunks, num_keywords=5):
    topics = lda_model.print_topics(num_words=num_keywords)
    topic_keywords = [" ".join([word.split("*")[1].strip().strip('"') for word in topic[1].split("+")[:num_keywords]]) 
                      for topic in topics]
    
    doc_bow = dictionary.doc2bow(tokenize_chinese(" ".join(chunks)))
    doc_topics = lda_model.get_document_topics(doc_bow)
    
    main_topic = max(doc_topics, key=lambda x: x[1])
    main_topic_keywords = topic_keywords[main_topic[0]]
    
    # 生成分类标签
    tags = set()
    for keywords in topic_keywords:
        tags.update(keywords.split())
    
    metadata = {
        "main_topic": f"Topic {main_topic[0]}",
        "topic_probability": main_topic[1],
        "keywords": main_topic_keywords,
        "all_topics": {f"Topic {i}": kw for i, kw in enumerate(topic_keywords)},
        "tags": list(tags)
    }
    
    return metadata

def main(docx_path, output_dir):
    # 1. 转换DOCX到结构化内容
    structured_content = docx_to_structured_markdown(docx_path, output_dir)
    
    # 2. 生成Markdown
    markdown_content = generate_markdown(structured_content, output_dir)
    
    # 3. 实现多种分块策略
    chunk_strategies = ["paragraph", "sentence", "fixed_length"]
    chunks = {strategy: chunk_text(markdown_content, strategy) for strategy in chunk_strategies}
    
    # 4. 中文分词和嵌入
    model = SentenceTransformer('distiluse-base-multilingual-cased-v2')  # 支持繁体中文的模型
    embedded_chunks = {}
    
    for strategy, chunk_list in chunks.items():
        embedded_chunks[strategy] = []
        for chunk in chunk_list:
            tokenized_chunk = " ".join(tokenize_chinese(chunk))
            embedding = embed_text(tokenized_chunk, model)
            embedded_chunks[strategy].append({
                'text': chunk,
                'embedding': embedding.tolist()
            })
    
    # 5. 使用LDA生成metadata
    lda_model, dictionary = apply_lda(chunks['paragraph'])
    metadata = generate_metadata(lda_model, dictionary, chunks['paragraph'])
    
    # 6. 保存结果
    result = {
        'metadata': metadata,
        'embedded_chunks': embedded_chunks
    }
    
    with open(os.path.join(output_dir, "rag_data.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    docx_path = "path/to/your/document.docx"
    output_dir = "path/to/output/directory"
    main(docx_path, output_dir)