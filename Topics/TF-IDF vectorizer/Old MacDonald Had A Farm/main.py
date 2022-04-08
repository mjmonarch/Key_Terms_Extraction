from sklearn.feature_extraction.text import TfidfVectorizer

dataset = open('./data/dataset/input.txt', 'r')

vectorizer = TfidfVectorizer(input='file')
weighted_matrix = vectorizer.fit_transform([dataset])
terms = vectorizer.get_feature_names()

print(weighted_matrix[(0, 10)])