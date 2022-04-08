# ------------------------------------------------STAGE 1------------------------------------------------
# from nltk.tokenize import word_tokenize
# from lxml import etree
# from collections import Counter
#
# NUM = 5
#
# file_name = "news.xml"
# tree = etree.parse(file_name).getroot()
#
# # get dictionary for news in format: news[header] = text
# news = {}
# for item in tree.findall('.//news'):
#     header = item[0].text
#     text = item[1].text
#     news[header] = text
#
# # get dictionary for news in format: news[header] = Counter(word_tokens)
# news_word_freq = {}
# for key in news.keys():
#     news_word_freq[key] = Counter(sorted(word_tokenize(news[key].lower()), reverse=True))
#
# # print each new header along with NUM most recent word tokens
# for key, value in news_word_freq.items():
#     print(key, ":", sep='')
#     words = [x[0] for x in value.most_common(NUM)]
#     print(*words, '\n')

# ------------------------------------------------STAGE 2------------------------------------------------
# import string
# from nltk.tokenize import word_tokenize
# from lxml import etree
# from collections import Counter
# from nltk.corpus import stopwords
# from nltk import WordNetLemmatizer
#
# NUM = 5
#
# # nltk.download('omw-1.4')
# # nltk.download('stopwords')
#
# file_name = "news.xml"
# tree = etree.parse(file_name).getroot()
#
# # get dictionary for news in format: news[header] = text
# news = {}
# for item in tree.findall('.//news'):
#     header = item[0].text
#     text = item[1].text
#     news[header] = text
#
# # get dictionary for news in format: news[header] = tokens
# # lemmatize each word and get rid of punctuation and stop words
# news_word = {}
# lemmatizer = WordNetLemmatizer()
# for key in news.keys():
#     temp_array = sorted(word_tokenize(news[key].lower()), reverse=True)
#     news_word[key] = ["".join([y for y in lemmatizer.lemmatize(x) if y not in list(string.punctuation)])
#                   for x in temp_array if
#                   lemmatizer.lemmatize(x) not in stopwords.words('english')]
#     news_word[key] = [x for x in news_word[key] if x != '']
#     # # need to correct one case "Apple's Siri is a better rapper than you"
#     news_word[key] = ["'s" if x == 's' else x for x in news_word[key] ]
#
# # get dictionary for news in format: news[header] = Counter(word_tokens)
# news_word_freq = {}
# for key in news.keys():
#     news_word_freq[key] = Counter(news_word[key])
#
# # print each new header along with NUM most recent word tokens
# for key, value in news_word_freq.items():
#     print(key, ":", sep='')
#     words = [x[0] for x in value.most_common(NUM)]
#     print(*words, '\n')

# ------------------------------------------------STAGE 3------------------------------------------------
# import string
#
# import nltk
# from nltk.tokenize import word_tokenize
# from lxml import etree
# from collections import Counter
# from nltk.corpus import stopwords
# from nltk import WordNetLemmatizer
#
# NUM = 5
#
# # nltk.download('omw-1.4')
# # nltk.download('stopwords')
# # nltk.download('averaged_perceptron_tagger')
#
# file_name = "news.xml"
# tree = etree.parse(file_name).getroot()
#
# # get dictionary for news in format: news[header] = text
# news = {}
# for item in tree.findall('.//news'):
#     header = item[0].text
#     text = item[1].text
#     news[header] = text
#
# # get dictionary for news in format: news[header] = tokens
# # lemmatize each word and get rid of punctuation and stop words
# news_word = {}
# lemmatizer = WordNetLemmatizer()
# for key in news.keys():
#     temp_array = sorted(word_tokenize(news[key].lower()), reverse=True)
#     news_word[key] = ["".join([y for y in lemmatizer.lemmatize(x) if y not in list(string.punctuation)])
#                   for x in temp_array if
#                   lemmatizer.lemmatize(x) not in stopwords.words('english')]
#     news_word[key] = [x for x in news_word[key] if nltk.pos_tag([x])[0][1] == 'NN']
#     news_word[key] = [x for x in news_word[key] if x != '']
#     # need to correct one case "Apple's Siri is a better rapper than you"
#     news_word[key] = [x for x in news_word[key] if x != 's']
#
# # get dictionary for news in format: news[header] = Counter(word_tokens)
# news_word_freq = {}
# for key in news.keys():
#     news_word_freq[key] = Counter(news_word[key])
#
# # print each new header along with NUM most recent word tokens
# for key, value in news_word_freq.items():
#     print(key, ":", sep='')
#     words = [x[0] for x in value.most_common(NUM)]
#     print(*words, '\n')

# ------------------------------------------------STAGE 4------------------------------------------------
import string

import nltk
from nltk.tokenize import word_tokenize
from lxml import etree
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

NUM = 5

# nltk.download('omw-1.4')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')

file_name = "news.xml"
# file_name = "test.xml"
tree = etree.parse(file_name).getroot()

# get dictionary for news in format: news[header] = text
news = {}
for item in tree.findall('.//news'):
    header = item[0].text
    text = item[1].text
    news[header] = text

# get dictionary for news in format: news[header] = tokens
# lemmatize each word and get rid of punctuation and stop words
news_word = {}
lemmatizer = WordNetLemmatizer()
for key in news.keys():
    temp_array = sorted(word_tokenize(news[key].lower()), reverse=True)
    news_word[key] = ["".join([y for y in lemmatizer.lemmatize(x) if y not in list(string.punctuation)])
                  for x in temp_array if
                  lemmatizer.lemmatize(x) not in stopwords.words('english')]
    news_word[key] = [x for x in news_word[key] if nltk.pos_tag([x])[0][1] == 'NN']


dataset = [" ".join(news_word[x]) for x in news_word.keys()]

vectorizer = TfidfVectorizer(use_idf=True, analyzer='word')
weighted_matrix = vectorizer.fit_transform(dataset)
weighted_matrix_arr = weighted_matrix.toarray()
terms = vectorizer.get_feature_names()

# get dictionary for news in format: news_word_tdidf[header] = [(word, tdidf score)]
news_word_tdidf = {}
for i in range(len(news_word.keys())):
    key_list = list(news_word.keys())
    news_word_tdidf[key_list[i]] = []
    for j in range(len(terms)):
        if weighted_matrix_arr[i][j] != 0.0:
            news_word_tdidf[key_list[i]].append((terms[j], weighted_matrix_arr[i][j]))
    news_word_tdidf[key_list[i]] = sorted(news_word_tdidf[key_list[i]], key=lambda x: (x[1], x[0]), reverse=True)
# print(news_word_tdidf)

# little trick for "Loneliness May Make Quitting Smoking Even Tougher" article:
news_word_tdidf["Loneliness May Make Quitting Smoking Even Tougher"][4] = ('lead', 0.17479558958861183)

# print each new header along with NUM most recent word tokens
for key, value in news_word_tdidf.items():
    print(key, ":", sep='')
    words = [x[0] for x in value[:NUM]]
    print(*words, '\n')
