import sys
import shelve
from nltk.tokenize import sent_tokenize,word_tokenize

#単語とその出現頻度の辞書型オブジェクト
word_count = {}

#shelveオブジェクト(単語とそのインデックスを格納)を開く
dic=shelve.open('shelve_test')
#カウント用変数に、shelveに格納されている要素(単語)数+1を代入
i = len(dic) +1

#単語とそのインデックスを格納する辞書型オブジェクト
display_object = {}

#読み込んだファイルの全文をsent_tokenizeでリストにして1文ずつループ(sentenceは各文が格納されるの文字列型オブジェクト)
for sentence in (sent_tokenize(open(sys.argv[1],'r').read())):
   for word in word_tokenize(sentence):
      #まだ出現していない単語のときにインデックスを付与
      if word not in dic:
         #shelveに単語とそのインデックスを追加         
         dic[word]=i
         i=i+1

      #頻度カウント用のオブジェクトに格納済みのとき
      if word in word_count:
         word_count[word]=word_count[word]+1
      #頻度カウント用オブジェクトに無い単語のとき
      else:
         word_count[word]=1

#インデックス順に辞書型オブジェクトに格納
for word in dic:
   #今回のファイルに含まれている単語のみ
   if word in word_count:
      #キー=出現順、値=出現頻度
      display_object[dic[word]]=word_count[word]
      #print(display_object[dic[word]])

#shelveを閉じる
dic.close()

#display_objectを文字列に変換して表示
for index,value in sorted(display_object.items(),key=lambda x:(x[0])):
   #display_objectのキー(インデックス)と値(頻度)を取り出し、連結して表示
   print(str(index)+":"+str(value),end=" ")

   
#最後に改行
print("")
