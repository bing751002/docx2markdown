import re

class Chunker:
    @staticmethod
    def fixed_length(text, chunk_size=1000):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    @staticmethod
    def paragraph(text):
        return text.split("\n\n")

    @staticmethod
    def sentence(text):
        return re.split(r'(?<=[.!?]) +', text)