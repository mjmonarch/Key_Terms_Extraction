from nltk.stem import LancasterStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

stemmer = LancasterStemmer()
for word in sent:
    print(stemmer.stem(word))
