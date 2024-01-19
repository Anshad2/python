# methods of set
colors={"red","green","blue"}

# insertion by add()= adding
colors.add("yellow")
print(colors)

# intersectopn  (common in two set)
st1={"red","green","blue"}
st2={"purple","yellow","cyan","blue","red"}
inter_set=st1.intersection(st2)
print(inter_set)

# union=combination of two set no duplication
union_set=st1.union(st2)
print(union_set)

# difrence set
diffe_set=st1.difference(st2)
print(diffe_set)

# to remve pop() 
st1.pop()
print(st1)

# remove()
colors.remove("red")
print(colors)

# discard() used to remove 
colors.discard("red")
print(colors)

#symmetric diffrence

# update()
st1={10,20,30}
st2={100,200,300}
st1.update(st2)
print(st1)
