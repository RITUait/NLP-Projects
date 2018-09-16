#Stop words

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

example_sentence = "This is an example sentence to show you, how it is working."
stop_words = set(stopwords.words("English"))
filtered_sentence = []

example_tokenize = word_tokenize(example_sentence)

print(example_tokenize)

#for w in example_tokenize:
 #   if w not in stop_words:
  #      filtered_sentence.append(w)


#print(filtered_sentence)
  #Or

filtered_sentence = [w for w in example_tokenize if not w in stop_words]
print(filtered_sentence)
