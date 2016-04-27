import CaboCha

c=CaboCha.Parser()
sentence="豊工にいっています。"

tree=c.parse(sentence)

phrase=tree.toString(CaboCha.FORMAT_TREE)
print(phrase)
lattice=tree.toString(CaboCha.FORMAT_LATTICE)
print(lattice.split("\n"))

for word in lattice.split("\n"):
    if word =="*":
        print("")
    else:
        print(word,end="")
#for i in tree.toString(CaboCha.FORMAT_LATTICE):
#    print(i)


#for i in range(tree.token_size()):
#    token = tree.token(i)
#    print ('Surface:', token.surface,token.ne)
    
#tree=c.parse(sentence)

#for i in range(tree.chunk_size()):
#    chunk=tree.chunk(i)
#    print(chunk.toString(CaboCha.FORMAT_TREE))
    #for j in range(chunk.token_pos,chunk.token_pos+chunk.token_size):
       # print(tree.token(j).surface)

#print(tree.toString(CaboCha.FORMAT_TREE))
