# class list

#1 def append()= add  a word to current list that shown in last word
orders=["friedrice","gheeroast","vb","cb","bb","mutton","cb","vb","cb","cb","vb"]
orders.append("tea")#only one argument is added
print(orders)

#2 def count()=count passed object by number eg cb=4
print(orders.count("cb"))

#3 index()= position
print(orders.index("gheeroast"))

#4 pop()= removed last object only
print(orders.pop())
print(orders)

#5 pop(x)= specific index removed
print(orders.pop(2))
print(orders)

#6 insert()=insert word to specific index
print(orders.insert(2,"goby"))
print(orders)

#7 remove()=specific object delet not index position but only first passed object removed
print(orders.remove("vb"))
print(orders)

#8 copy()=to get copy
ans_fvt_colours=["blue","yellow","green","white"]
res_fvt_colours=ans_fvt_colours.copy()
res_fvt_colours.remove("yellow")
print(ans_fvt_colours)
print(res_fvt_colours)

#9 reverse()
ans=["bro","sis","dad","mom","grand"]
print(ans.reverse())
print(ans)

#10 sort=sort
ans_fvt_colours.sort(reverse=True)
print(ans_fvt_colours)

# find duplicat number# important
arr=[4,9,5,6,9,5,4]
arr.sort()
count=1
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        ith_loca_elmnt=arr[i]
        jth_loca_elmnt=arr[j]
        diff=ith_loca_elmnt-jth_loca_elmnt
        if diff==0:
            print(ith_loca_elmnt)
            break
        count+=1
print(f"total{count}")
    

# by using while loop
arr=[4,9,5,6,9,5,4]
arr.sort()
i=0
while(i<len(arr)-1):
    j=i+1
    ith_loca_elmnt=arr[i]
    jth_loca_elmnt=arr[j]
    diff=jth_loca_elmnt-ith_loca_elmnt
    if diff==0:
        print(ith_loca_elmnt)
        i=j
    i+=1


# 
# find missing positive num #importent
arr=[1,4,3,5,6,7]
arr.sort()
i=0
while(i<len(arr)-1):
    j=i+1
    ith_loca_elmnt=arr[i]
    jth_loca_elmnt=arr[j]
    diff=jth_loca_elmnt-ith_loca_elmnt
    if (diff!=1):
        print(f"{ith_loca_elmnt+1} element is missing")
        break
    i+=1


