
# 1. Write a Python program to find the second largest number in a list.

lst=[]
for i in range(6):
  num=int(input("enter the number"))
  lst.append(num)
lst.sort()
print("the second largesr elemnt is:",lst[-2])# negative indices two


# or
# lst=[10,20,30,40,50,60]
# new_lst=set(lst)
# new_lst.remove(max(new_lst))
# print(max(new_lst))

# or
# numbers=[1,3,5,7,9,5,8]
# numbers.sort()
# print("the second largest number is : ", numbers[-2])

# 2. Write a program to filter the dictionary, from a dictionary of people’s heights
#  and you wanted to filter out anyone below a certain height.
# Let’s filter out anyone less than 170cm.

people={"ansh":168,"gopu":189,"manu":167,"kochu":190,"resh":186,
        "anja":170,"ainu":167,"kunju":160,"alice":187}
for k,v in people.items():
    if v < 170:
        print(k,v)

# filterd_height={}
# for name,height in people.items():
#     if height < 170:
#         filterd_height[name]=height
# print(filterd_height)

# 3. Pattern print 
#     4 4 4 4 4 4 4  
#     4 3 3 3 3 3 4   
#     4 3 2 2 2 3 4   
#     4 3 2 1 2 3 4   
#     4 3 2 2 2 3 4   
#     4 3 3 3 3 3 4   
#     4 4 4 4 4 4 4

# n=4
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         print(max(abs(n-i-1),abs(n-j-1))+ 1,end=" ")
#     print()

n=4

s = 2 * n - 1
    # Upper Half 
for i in range(0, int(s / 2)):  
    m = n 
    # Decreasing part 
    for j in range(0, i): 
        print(m ,end= " " )
        m-=1  
    # Constant Part 
    for k in range(0, s - 2 * i):
        print(n-i ,end= " " )
    # Increasing part. 
    m = n - i + 1
    for l in range(0, i): 
        print(m ,end= " " ) 
        m+=1  
    print("")

# Lower Half 
for i in range(int(s / 2),-1,-1): 
    # Decreasing Part 
    m = n 
    for j in range(0, i):
        print(m ,end= " " )
        m-=1
    # Constant Part. 
    for k in range(0, s - 2 * i):
        print(n-i ,end= " " )
    # Decreasing Part 
    m = n - i + 1
    for l in range(0, i): 
        print(m ,end= " " ) 
        m+=1    
    print("")