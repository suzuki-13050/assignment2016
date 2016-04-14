import sys
import os.path

file_name=sys.argv[1]
#ファイルが存在するかどうか
if (os.path.isfile(file_name)):
    #辞書登録
    wordcount={}
    
    for line in open(file_name, 'r'):
        for word in line.split():
            #登録済みか
            if word in wordcount:
                 wordcount[word]=wordcount[word]+1
            else:
                 wordcount[word]=1

    #辞書内のキーでループ
    for index in wordcount:
        print(wordcount.setdefault(index),index,end='\n')
