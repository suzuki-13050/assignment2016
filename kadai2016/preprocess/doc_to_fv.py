import sys
import shelve
from nltk.tokenize import sent_tokenize,word_tokenize

#単語とその出現頻度の辞書型オブジェクト
word_count={}
#単語とその出現順の辞書型オブジェクト
word_list={}
#bag-of-word表現による素性ベクトルの辞書型オブジェクト
bow_vector={}

#カウント用変数、初期値1
i=1

#読み込んだファイルの全文をsent_tokenizeでリストにして1文ずつループ(sentenceは各文が格納されるの文字列型オブジェクト)
for sentence in (sent_tokenize(open(sys.argv[1],'r').read())):
   for word in word_tokenize(sentence):
      #まだ出現していない単語のとき
      if word not in word_list:
         word_list[word]=i
         i=i+1
      #頻度カウント用のオブジェクトに格納済みのとき
      if word in word_count:
         word_count[word]=word_count[word]+1
      #頻度カウント用オブジェクトに無い単語のとき
      else:
         word_count[word]=1

#shelveオブジェクトを作る
dic=shelve.open('shelve_test')
#単語の出現順をデータベース(永続)化
dic.update(word_list)

for index in word_list:
   #キー=出現順、値=出現頻度
   bow_vector[dic[index]]=word_count[index]

#shelveを閉じる
dic.close()

#bow_vectorを文字列に変換して表示
for index in bow_vector:
   #bow_bectorのキーと値を取り出し、連結して表示
   word=str(index)+":"+str(bow_vector[index])
   print(word,end=" ")

#最後に改行
print("")
