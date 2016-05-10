import gzip
import MeCab
import sys
from nltk.tokenize import RegexpTokenizer

jp_sent_tokenizer=RegexpTokenizer(u'[^！？。]*[！？。]?')
lines=gzip.open(sys.argv[1],'r').read().decode("utf-8").split()

sentences=jp_sent_tokenizer.tokenize(lines[0])

tagger=MeCab.Tagger()
tagger.parse('') #バグ回避

word_index={} #単語とインデックス(出現順)が格納される辞書型オブジェクト
bow={} #素性ベクトル(bag-of-words)格納用オブジェクト
i=1 #インデックス初期値=1
hit=("名詞","動詞","形容詞","形容動詞","副詞") #内容語

for sentence in sentences:
    node=tagger.parseToNode(sentence)
    while node:
        kind=node.feature.split(",")[0] #"現在の単語の品詞"
        if node.surface !="" and kind in hit : #BOS/EOS以外で、内容語である単語のみ
            if node.surface in word_index:
                bow[word_index[node.surface]]+=1
            else:
                word_index[node.surface]=i
                i=i+1
                
                bow[word_index[node.surface]]=1

            #print(kind)
        node = node.next
        

print(sorted(word_index.items(),key=lambda x:(x[1])))
print(sorted(bow.items(),key=lambda x:(x[0])))

