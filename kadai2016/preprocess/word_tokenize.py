import sys
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

for index in (sent_tokenize(open(sys.argv[1],'r').read())):
   print(word_tokenize(index))
