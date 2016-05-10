import gzip
import MeCab
import sys
from nltk.tokenize import RegexpTokenizer

jp_sent_tokenizer=RegexpTokenizer(u'[^！？。]*[！？。]?')
lines=gzip.open(sys.argv[1],'r').read().decode("utf-8").split("\n")

sentences=jp_sent_tokenizer.tokenize(lines[0])

tagger=MeCab.Tagger()
tagger.parse('') #バグ回避

word_index={} #単語とインデックス(出現順)が格納される辞書型オブジェクト
bow={} #素性ベクトル(bag-of-words)格納用オブジェクト
i=1 #インデックス初期値=1
#hit=("名詞","動詞","形容詞","形容動詞","副詞") #内容語

def index_grant(i,node,num):
    sur=""
    for j in range(num):
        #最後以外なら
        if node != None:
            sur=sur+node.surface
            node=node.next
    
    if sur not in word_index:#未登録語=インデックス追加、カウント1
        word_index[sur]=i
        i=i+1

    if word_index[sur] in bow:
        bow[word_index[sur]]+=1
    else:
        bow[word_index[sur]]=1
        
    #インデックス番号を返す
    return i

for line in lines:
    sentences=jp_sent_tokenizer.tokenize(line)
    for sentence in sentences:
        node=tagger.parseToNode(sentence)
        while node:
            kind=node.feature.split(",")[0] #"現在の単語の品詞"
            if node.surface !="":  #and kind in hit : #BOS/EOS以外で、内容語である単語のみ
                i=index_grant(i,node,1)#unigram
                i=index_grant(i,node,2)#bygram
                i=index_grant(i,node,3)#trygram
            node=node.next
    
    #1行分の素性ベクトル表示
    for vector in sorted(bow.items(),key=lambda x:(x[0])):
        print(str(vector[0])+":"+str(vector[1]),end=" ")
    
    bow={}#素性ベクトルのリセット
    print("")#1行分出力毎に改行
    
#print(sorted(word_index.items(),key=lambda x:(x[1])))
#print(sorted(bow.items(),key=lambda x:(x[0])))
