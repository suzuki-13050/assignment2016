import sys
import os.path

#読み込み用ファイル
file_name=sys.argv[1]
#書き込み用ファイル
search_word=sys.argv[2]

#ファイルが存在するかどうか
if (os.path.isfile(file_name)):
    F = open(file_name, 'r', encoding="utf-8")
    flg = True
else:
    flg = False

if (flg == True):
    for line in F:
        #lineにsearch_wordの文字列が含まれていればTrue
        if (search_word in line):
             print(line,end="")
        
F.close