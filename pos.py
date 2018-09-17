#Parts of speech tagging...
#Its a really cool thing. I love it very much. :)
#===using simple tokenizer====

import nltk
from nltk import word_tokenize

new_text = "Hello Ms. Ritu, Hows your day? "


def process():
    for i in new_text:
        token = word_tokenize(new_text)
        tagged = nltk.pos_tag(token)
    print(tagged)

process()        

#output will be : [('Hello', 'NNP'), ('Ms.', 'NNP'), ('Ritu', 'NNP'),(',', ','),
#                  ('Hows', 'NNP'), ('your', 'PRP$'), ('day', 'NN'), ('?', '.')]

#====using custom_tokenizer====
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_data():
    for i in tokenized:
        words = word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)

process_data()    

#Output will be
#=======
[('Today', 'NN'), (',', ','), ('having', 'VBG'), ('come', 'VBN'), ('far', 'RB'), ('in', 'IN'), ('our', 'PRP$'), ('own', 'JJ'), ('historical', 'JJ'), ('journey', 'NN'), (',', ','), ('we', 'PRP'), ('must', 'MD'), ('decide', 'VB'), (':', ':'), ('Will', 'MD'), ('we', 'PRP'), ('turn', 'VB'), ('back', 'RP'), (',', ','), ('or', 'CC'), ('finish', 'VB'), ('well', 'RB'), ('?', '.')]
[('Before', 'IN'), ('history', 'NN'), ('is', 'VBZ'), ('written', 'VBN'), ('down', 'RP'), ('in', 'IN'), ('books', 'NNS'), (',', ','), ('it', 'PRP'), ('is', 'VBZ'), ('written', 'VBN'), ('in', 'IN'), ('courage', 'NN'), ('.', '.')]
[('Like', 'IN'), ('Americans', 'NNPS'), ('before', 'IN'), ('us', 'PRP'), (',', ','), ('we', 'PRP'), ('will', 'MD'), ('show', 'VB'), ('that', 'DT'), ('courage', 'NN'), ('and', 'CC'), ('we', 'PRP'), ('will', 'MD'), ('finish', 'VB'), ('well', 'RB'), ('.', '.')]
[('We', 'PRP'), ('will', 'MD'), ('lead', 'VB'), ('freedom', 'NN'), ("'s", 'POS'), ('advance', 'NN'), ('.', '.')]
[('We', 'PRP'), ('will', 'MD'), ('compete', 'VB'), ('and', 'CC'), ('excel', 'VB'), ('in', 'IN'), ('the', 'DT'), ('global', 'JJ'), ('economy', 'NN'), ('.', '.')]
[('We', 'PRP'), ('will', 'MD'), ('renew', 'VB'), ('the', 'DT'), ('defining', 'VBG'), ('moral', 'JJ'), ('commitments', 'NNS'), ('of', 'IN'), ('this', 'DT'), ('land', 'NN'), ('.', '.')]
[('And', 'CC'), ('so', 'RB'), ('we', 'PRP'), ('move', 'VBP'), ('forward', 'RB'), ('--', ':'), ('optimistic', 'JJ'), ('about', 'IN'), ('our', 'PRP$'), ('country', 'NN'), (',', ','), ('faithful', 'JJ'), ('to', 'TO'), ('its', 'PRP$'), ('cause', 'NN'), (',', ','), ('and', 'CC'), ('confident', 'NN'), ('of', 'IN'), ('the', 'DT'), ('victories', 'NNS'), ('to', 'TO'), ('come', 'VB'), ('.', '.')]
[('May', 'NNP'), ('God', 'NNP'), ('bless', 'NN'), ('America', 'NNP'), ('.', '.')]
[('(', '('), ('Applause', 'NNP'), ('.', '.'), (')', ')')]
#======
