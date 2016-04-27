import sys
import MeCab

tagger=MeCab.Tagger()


for sentence in tagger.parse("豊工に行っています。").split("\n"):
    i=1
    for words in sentence.split(","):
        if i in [1,7]:
            print(words,end=" ")
        i=i+1
    #一行分出力したら改行
    print("")
