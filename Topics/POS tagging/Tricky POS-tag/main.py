import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

tagged_text = nltk.pos_tag(sent)
for item in tagged_text:
    if item[0] == 'raced':
        print(item[1])
