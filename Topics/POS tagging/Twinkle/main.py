import nltk

# nltk.download('averaged_perceptron_tagger')

poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']

tagged_text = nltk.pos_tag(poem)
for item in tagged_text:
    if item[1] == 'NN':
        print(item[0])
