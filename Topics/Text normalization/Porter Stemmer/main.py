from nltk.stem import PorterStemmer

word = input()
stemmer = PorterStemmer()
print(stemmer.stem(word))
