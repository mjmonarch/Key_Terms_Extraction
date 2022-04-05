# ------------------------------------------------STAGE 1------------------------------------------------
from nltk.tokenize import word_tokenize
from lxml import etree
from collections import Counter

NUM = 5

# file_name = input()
file_name = "news.xml"
tree = etree.parse(file_name).getroot()

# get dictionary for news in format: news[header] = text
news = {}
for item in tree.findall('.//news'):
    header = item[0].text
    text = item[1].text
    news[header] = text

# get dictionary for news in format: news[header] = Counter(word_tokens)
news_word_freq = {}
for key in news.keys():
    news_word_freq[key] = Counter(sorted(word_tokenize(news[key].lower()), reverse=True))

# print each new header along with NUM most recent word tokens
for key, value in news_word_freq.items():
    print(key, ":", sep='')
    words = [x[0] for x in value.most_common(NUM)]
    print(*words, '\n')
