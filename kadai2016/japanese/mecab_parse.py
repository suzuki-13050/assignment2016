import MeCab

tagger=MeCab.Tagger()
print(tagger.parse("豊工に行っています。"))
