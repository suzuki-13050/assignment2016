import sys
import nltk
from nltk.tokenize import sent_tokenize

print(sent_tokenize(open(sys.argv[1],'r').read()))

#readを使わない場合
#print(sent_tokenize(nltk.filestring(open(file_path[1],'r'))))
