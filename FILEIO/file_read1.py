f=open("C:\\Users\\user\\Desktop\\my python\\fileio\\new.text","r")

#total number of words
wc={}
for line in f:
  words=line.rstrip("\n").split(" ")
  for w in words:
     if w in wc:
        wc[w]+=1
     else:
      wc[w]=1
print(wc)
