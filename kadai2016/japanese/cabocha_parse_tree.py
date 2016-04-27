import CaboCha

tagger=CaboCha.Parser()
print(tagger.parse("豊工にいっています。").toString(CaboCha.FORMAT_TREE))
