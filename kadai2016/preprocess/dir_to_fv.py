import sys
import shelve
import os
from nltk.tokenize import sent_tokenize,word_tokenize

#引数1：読込ディレクトリ、引数2：ラベル

#shelveオブジェクト(単語とそのインデックスを格納)を開く
dic=shelve.open('shelve_test')
#カウント用変数に、shelveに格納されている要素(単語)数+1を代入
i = len(dic) +1

#カレントディレクトリからの相対パスを取得
work_path=os.path.relpath(sys.argv[1],os.getcwd())+"/"
#os.chdir(work_path)
#work_path=os.chdir(os.path.abspath(sys.argv[1]))

#ディレクトリ内のファイル名を取得して、ファイル名順番に処理
if os.path.isdir(work_path):
   for file_name in sorted(os.listdir(work_path)):
      #単語とその出現頻度の辞書型オブジェクト
      word_count = {}
      #単語とそのインデックスを格納する辞書型オブジェクト
      display_object = {}
   
      #読込ファイルの全文をsent_tokenizeでリスト化>1文ずつループ(sentenceは各文が格納されるリスト型オブジェクト)
      for sentence in sent_tokenize(open(work_path+file_name,'r').read()):
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

            #インデックスに対応した頻度を辞書型に格納
            display_object[dic[word]]=word_count[word]

      #ラベルを添付
      print(sys.argv[2],end=" ")
      
      #インデックス順にインデックスとその頻度を表示
      for index,value in sorted(display_object.items(),key=lambda x:(x[0])):
         print(str(index)+":"+str(value),end=" ")
      print("")

#shelveを閉じる
dic.close()
