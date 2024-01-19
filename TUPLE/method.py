
# tuple
# define()
# insertion order preserved
# duplicates allowed
# updates not possible (immutable)
# same aas list expect updation
tp=(10,20,30,40,20,10)
# tp[0]=100 not possible that is updates not posible
print(tp)
colour=("red",)# if it have one word put it in " " , and given comma , then only it become tupple
print(type(colour))

colour=("red")# this is string
print(type(colour))

# only count and index
# count()=to count passed obeject
print(tp.count(10))
# index()= position of passed object
print(tp.index(40))

