#Stemming 
#e.g. after stemming of "Reading" , the stem obtained will be "Read".

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythonly","pythoner","pythoning"]

for w in example_words:
    print(ps.stem(w))

new_text = "it is very important to be pythonly while you are pythoning in python.Pythoners perform good at pythoning."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

