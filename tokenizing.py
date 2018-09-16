#Tokenizing words and sentences

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "hello Ms. Ritu, I love Programming. Well, apart from this i like reading novels. What about you? Amm.. well also travelling to new places and most importantly talking to really knowledgable people, if available any."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
   print(i)



