from sklearn.feature_extraction.text import TfidfVectorizer

dataset = ["Load up on guns, bring your friends",
           "It's fun to lose and to pretend",
           "She's over-bored and self-assured",
           "Oh no, I know a dirty word",
           "Hello"]

vectorizer = TfidfVectorizer()
weighted_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names()

# your code here