import sys
import os.path

file_name=sys.argv[1]
#ファイルが存在するかどうか
if (os.path.isfile(file_name)):
    F = open(file_name, 'r', encoding="utf-8")
    for line in F:
        #末尾文字を空白のみで指定(空白で改行)
        print(line, end=" ")
F.close()