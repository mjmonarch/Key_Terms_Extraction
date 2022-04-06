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
import string
import nltk
from nltk.tokenize import word_tokenize
from lxml import etree
from collections import Counter
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer

NUM = 5

# nltk.download('omw-1.4')
# nltk.download('stopwords')

file_name = "news.xml"
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
    # news_word[key] = [lemmatizer.lemmatize(x) for x in temp_array]
    # news_word[key] = ["".join([y for y in x if y not in list(string.punctuation)])
    #                   for x in news_word[key] if
    #                   news_word[key] not in stopwords.words('english')]

    # news_word[key] = [x for x in news_word[key] if x not in stopwords.words('english')]
    # news_word[key] = ["".join([y for y in news_word[key] if y not in list(string.punctuation)])
    #                   for x in news_word[key]]
    news_word[key] = [x for x in news_word[key] if x != '']
    news_word[key] = ["'s" if x == 's' else x for x in news_word[key] ]

# get dictionary for news in format: news[header] = Counter(word_tokens)
news_word_freq = {}
for key in news.keys():
    news_word_freq[key] = Counter(news_word[key])

# # need to correct one case
# print(news_word_freq["Apple's Siri is a better rapper than you"])
# # news_word_freq["Apple's Siri is a better rapper than you"][0] = "'s"
# print(news_word_freq["Apple's Siri is a better rapper than you"])

# print each new header along with NUM most recent word tokens
for key, value in news_word_freq.items():
    print(key, ":", sep='')
    words = [x[0] for x in value.most_common(NUM)]
    print(*words, '\n')
