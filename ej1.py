from newspaper import Article
import re
from collections import Counter

def body(url):
    article = Article(url)
    article.download()
    article.parse()
    lista = re.split(r'\W+',article.text)
    return Counter(lista)