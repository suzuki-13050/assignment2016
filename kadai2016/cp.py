import sys
import os.path

#読み込み用ファイル
file_name=sys.argv[1]
#書き込み用ファイル
save_file=sys.argv[2]

#ファイルが存在するかどうか
if (os.path.isfile(file_name)):
    F = open(file_name, 'r', encoding="utf-8")
    flg = True
else:
    flg = False

O = open(save_file, 'w')

if (flg == True):
    for line in F:
        O.write(line)

F.close
O.close
