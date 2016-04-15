import sys
from nltk.tokenize import sent_tokenize,word_tokenize

word_count={}
for sentence in (sent_tokenize(open(sys.argv[1],'r').read())):
   for word in word_tokenize(sentence):
      if word in word_count:
         word_count[word]=word_count[word]+1
      else:
         word_count[word]=1

for index in word_count:
   print(word_count[index],index)

