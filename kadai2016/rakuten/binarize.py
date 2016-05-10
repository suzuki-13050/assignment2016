import sys

for label in open(sys.argv[1],'r').read().split():
    if int(label) >= 4:
        print("1")
    else:
        print("-1")
