import sys
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tag import SennaTagger

tagger = SennaTagger('/usr/share/senna-v2.0')

#sys.argv[1]で指定されたファイルを読み込み
#文全体をリスト化、最初の文のみにする(sent_tokenize[0])
#単語毎のリストとして抽出(word_tokenize)>first_sentence
first_sentence=word_tokenize(sent_tokenize(open(sys.argv[1],'r').read())[0])
print(tagger.tag(first_sentence))


