import gzip
import sys
from nltk.tokenize import RegexpTokenizer

jp_sent_tokenizer=RegexpTokenizer(u'[^！？。]*[！？。]?')

f_sent=gzip.open(sys.argv[1],'r').read().decode("utf-8").split()[0]
print(jp_sent_tokenizer.tokenize(f_sent))

