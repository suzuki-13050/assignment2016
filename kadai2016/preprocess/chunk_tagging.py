import sys
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tag import SennaTagger,SennaChunkTagger

ctagger = SennaChunkTagger('/usr/share/senna-v2.0')
#辞書形式のオブジェクト定義

#sys.argv[1]で指定されたファイルを読み込み
#文全体をリスト化、最初の文のみにする(sent_tokenize[0])

first_sentence = sent_tokenize(open(sys.argv[1],'r').read())[0]
#first_sentence = word_tokenize(sent_tokenize(open(sys.argv[1],'r').read())[0])

#１文目をタグ付けした単語リストにする
taglist = ctagger.tag(first_sentence.split())

buff1=""

#taglistの単語とタグでループ
for word,tag in taglist:
    if "B-" in tag:
        if buff1 !="":
            #同じtabを持つwordと、tagの３文字目以降を表示
            print(buff1, buff2[2:])
        buff1=word
        buff2=tag
    elif "I-" in tag:
        buff1 = buff1 + " " + word
