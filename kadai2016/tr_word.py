import sys
import os.path

file_name=sys.argv[1]
#ファイルが存在するかどうか
if (os.path.isfile(file_name)):
    F = open(file_name, 'r', encoding="utf-8")
    for line in F:
        word=line.split( )
        for index in range(0,len(word)):
            print(word[index].strip(",- :.()"), end="\n")
        
F.close()
