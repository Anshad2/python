# list=[3,4,5,2]
# sum=8 (3,5)
# sum=7 (4,3)(5,2)
# two pair sum
#     0 1 2 3 4
list=[3,4,5,2,6]
list.sort()
sum=int(input("enter the sum"))
count=1
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        curr_sum=list[i]+list[j]
        if sum==curr_sum:
            print(list[i],list[j])
            break
        count+=1
print("loop count",count)

# worst count=print("loop count",count)


##### "interview question" #######

#    low      upper
list=[3,4,5,2,6]
list.sort()
sum=int(input("sum is"))
lower=0
count=0
upper=len(list)-1
while(lower<upper):
    curr_sum=list[lower]+list[upper]

    if curr_sum==sum:
        print(list[lower],list[upper])
        lower+=1
        upper-=1
    elif curr_sum<sum:
        lower+=1
    elif curr_sum>sum:
        upper-=1
    count+=1
print("loop count",count)







# largest number genrate from the list 9782312
list=[23,12,78,9]
list.sort()







        

