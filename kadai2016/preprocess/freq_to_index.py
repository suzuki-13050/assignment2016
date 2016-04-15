import sys
import shelve
from nltk.tokenize import sent_tokenize,word_tokenize

#単語とその出現頻度の辞書型オブジェクト
word_count={}
#単語とその出現順の辞書型オブジェクト
word_list={}


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

#for index in word_count:
   #print(word_count[index],index)
for index in word_list:
   #shelve内のキーとその内容を表示
   print(index,dic[index])
#shelveを閉じる
dic.close()
