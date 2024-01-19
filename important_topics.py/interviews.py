# # # # # if else
# # # # # loop for, while pattern
# # # # # dictionary,list

# # # # # sum of even numbers
# # # # # sum=0
# # # # # for num in range(2,51):
# # # # #     if num%2==0:
# # # # #      sum=sum+num
# # # # # print(sum)


# # # # # # while loop
# # # # # sum=0
# # # # # num=2
# # # # # while(num<=50):
# # # # #    if num%2==0:
# # # # #       print(num)
# # # # #       sum=sum+num
# # # # #       num+=2
# # # # # print(sum)


# # # # # num=10
# # # # # while(num>=-10):
# # # # #     print(num)
# # # # #     num-=2

# # # # # # sum of numbers from 1 to 100
# # # # # sum=0
# # # # # for i in range(1,101):
# # # # #     sum=sum+i
# # # # # print(sum)

# # # # # multiplication of seven
# # # # # mul=7
# # # # # for num in range(1,11):
# # # # #     res=num*mul
# # # # #     print(num,'*',mul,'=',res)
    
# # # # # factorial of number
# # # # # check=int(input("number"))
# # # # # fact=1
# # # # # for i in range(1,check+1):
# # # # #     fact=fact*i
# # # # # print(fact)

# # # # # fibanocci 0,1,1,2,3,5,8

# # # # # reverse number
# # # # original_digit=int(input("enter the digit"))
# # # # num=int(original_digit)
# # # # reversed=int(num[::-1])
# # # # print(reversed)

# # # # or
# # # # num=int(input("enter the number"))
# # # # reversed_num = 0
# # # # while num != 0:# loop that continue until num become zero
# # # #     digit = num % 10# get last digit
# # # #     reversed_num = reversed_num * 10 + digit
# # # #     num //= 10
# # # # print(f" the Reversed Number is {reversed_num}")


# # # # num=int(input("enter num"))
# # # # is_prime=True
# # # # for i in range(2,num):
# # # #     if num % i ==0:
# # # #         is_prime=False
# # # #         break
# # # # if is_prime:
# # # #     fact=1
# # # #     for i in range(1,num+1):
# # # #      fact=fact*i
# # # #     print(f"this is a prime number and its factorial is {fact}")
# # # # else:
# # # #    print("not a prime number")
    

# # #
# # # num=int(input("enter your number"))
# # # mul=0
# # # for i in range(1,11):
# # #   mul=num * i
# # #   print(f"{i} * {num} = {mul}")

# # # number=int(input("enter your number"))
# # # mul=0
# # # i=1
# # # while(i<=10):
# # #  mul=number * i
# # #  print(i, '*', number,'=', mul )
# # #  i+=1

# # rows=int(input("number of row"))# for number of rows
# # # n=5
# # for i in range(rows):#row
# #     for j in range(i+1):#coloumn
# #         print(i+1,end=" ")
# #     print()


# # input=input("enter your string:")
# # total_length=print(len(input))
# # word_count=0
# # digit_count=0
# # for ch in input:
# #     if ch.isdigit():
# #         digit_count+=1
# #     elif ch.isalpha():
# #         word_count+=1
# #     else:
# #         pass
# # print(f"word count is {word_count} and digit count is {digit_count}")

# x=("1234567")
# y=reversed(x)
# print(tuple(y))


# rows=int(input("number of row"))# for number of rows
# # n=5
# for i in range(1,rows+1):#row
#     for j in range(rows-i+1):#coloumn
#         print(i,end=" ")
#     print()

# my_list=[]
# positive=[]
# negative=[]
# n=int(input("enter"))
# for i in range(0,n):
#     values=int(input("enter values"))
#     my_list.append(values)
# print(my_list)
# for i in range(n):

#   if my_list[i]>=0:
#     positive.append(my_list[i])
#   else:
#     negative.append(my_list[i])
# print(my_list)
# print(positive)
# print(negative)


# 11111
# 2222
# 333
# 44
# 5

# n=5
# for i in range(1,n+1):
#     for j in range(n-i+1):
#         print(i,end=" ")
#     print()



# tpl=(12,34,56,76,88,90)
# lst=[]
# rev_lst=[]
# for num in tpl:
#     lst.append(num)
# for num in lst:
#     rev_lst.insert(0,num)
# print(rev_lst)

# tpl=(10,20,30,40,50)
# y=reversed(tpl)
# print(tuple(y))
# rows=int(input("number of row"))# for number of rows
# # n=5
# for i in range(1,rows+1):#row
#     for j in range(rows-i+1):#coloumn
#         print(i,end=" ")
#     print()

# my_lst=[]
# odd_lst=[]
# even_lst=[]
# len=int(input("length"))
# for i in range(0,len+1):
#     value=int(input("enter values"))
#     my_lst.append(value)
# for i in range(0,len):
#     if my_lst[i] % 2==0:
#         even_lst.append(my_lst[i])
#     else:
#         odd_lst.append(my_lst[i])
# print(my_lst)
# print(even_lst)
# print(odd_lst)


# num=int(input("num of row"))#how many rows want
# for i in range(0,num+1):#row
#    for  j in range(1,i+1):#coloumn
#     print("*",end=" ")
#    print()
# *
# * *
# * * *
# * * * *
# * * * * *
# n=int(input("number of row"))
# for i in range(n):#row
#     for j in range(n-i-1):#space
#         print(" ",end=" ")
#     for j in range(i+1):#coloumn
#         print("*",end=" ")
#     print()

# num=int(input("no of terms needed"))
# lst=[]
# for i in range(num):
#     value=int(input("enter values"))
#     lst.append(value)

# ass=lst.sort()
# print(lst)
# 


# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

# n=int(input("rows"))
# for i in range(n):#row
#     for j in range(n-i-1):#space
#         print(" ",end=" ")#gap
#     for j in range(i+1):#coloumn
#         print("*",end=" ")#what to print in coloumn
#     print()


# tpl=(10,20,30,40,50,60,70,80,90)
# rvs_lst=[]
# rvs_tpl=()
# for n in tpl:
#     rvs_lst.insert(0,n)
# rvs_tpl=tuple(rvs_lst)
# print(rvs_tpl)

# n=5
# for i in range(n):
#     print("*" *5)


# start_range=5
# end_range=30
# for i in range(3):
#     user_input=int(input(f"enter a num between {start_range} and {end_range} : "))
#     if start_range <= user_input <= end_range:
#         print(f"the {user_input} is given range")
#         break
#     else:
#         print(f"num {user_input} not given range")




# lst=[4,5,2,9,7,8,3,6]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)
# print(min(squares))

# lst1=["ant","man","cow","rat","mat","fat"]
# lst2=["hat","man","apple","vehicle","jump","fat"]
# print(set(lst1)& set(lst2))
# lst1.sort()
# lst2.sort()
# p1,p2=0,0
# while(p1<len(lst1) and p2<len(lst2)):
#     if lst1[p1]==lst2[p2]:
#      print(lst1[p1])
#      p1+=1
#      p2+=1
#     elif lst1[p1]< lst2[p2]:
#      p1+=1
#     else:
#      p2+=1

# list1=[12,11,55,77,88,66,33,44,6]
# list2=[1,2,5,44,66,88,22,4,6]

# for i in  (list1):
#     for j in  (list2):
#         if i==j :
#             print(i, end=" ")

# lst=[2,4,5,6,7,8,9]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)
# print(min(squares))


# n=6
# for i in range(n,0,-1):
#     for j in range(0,i):
#      print(i,end=" ")
#     print()

# decimal=int(input("enter number"))
# binary=""
# while decimal>0:
#     remainder=decimal % 2
#     binary=str(remainder)+binary
#     decimal=decimal // 2
# print(binary)

# lst=[]
# len_lst=int(input("enter length"))
# for i in range(len_lst):
#  user_input=int(input("enter the number"))
#  lst.append(user_input)
# print(lst)
# index=1
# while index < len(lst):
#     print(lst[index])
#     index+=2
# lst=[2,4,5,6,7,8,9]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)
# lst=[]
# sq_lst=[]
# cube_lst=[]
# for i in range(5):
#    user_input=int(input("enter number")) 
#    lst.append(user_input)
# for num in lst:
#    sq=num**2
#    cube=num**3
#    sq_lst.append(sq)
#    cube_lst.append(cube)

# print(lst)
# print(sq_lst)
# print(cube_lst)
# lst=[]
# for i in range(6):
#  user_input=int(input("enter the number"))
#  lst.append(user_input)
# print(lst)
# index=1
# while index < len(lst):
#     print(lst[index])
#     index+=2

employee={"id":1998,"name":"anshad","dept":"IT","salary":60000}
if "exp" in employee:
  print(employee.get("exp"))
else:
   print("key not found")




# num=5
# alph=65
# for i in range(num):
#     for j in range(num-i-1):# space
#         print("",end=" ")
#     for j in range(i+1):#col
#      print(chr(alph),end=" ")
#      alph+=1
#     print()

# num=[]
# cube=[]
# lst_of_tpl=[]
# limit=int(input("enter the limit of list"))
# for i in range(limit):
#     user_input=int(input("enter the number"))
# num.append(user_input)
#     cube.append(user_input**3)
#     lst_of_tpl.append((num,cube))
#     # lst_of_tpl.append(tuple(cube))
# print(lst_of_tpl)

# tpl=()
# my_lst=list(tpl)
# sum=0
# limit=int(input("enter the limit of tuple"))
# for i in range(limit+1):
#     user_input=int(input("enter number"))
#     my_lst.append(user_input)
#     sum=sum+user_input
# print(sum)
# tpl=(1,2,3,4,5,6,7)
# sum=0
# my_lst=list(tpl)
# for num in tpl:
#     sum=sum+num
# print(sum)
# n=5
# for i in range(0,n+1):#row
#    for  j in range(1,i+1):#coloumn
#     print("*",end=" ")
#    print()
# tpl=(1,2,3,4,5,7)
# tpl_sum=sum(tpl)
# print(tpl_sum)
# tpl=(1,2,3,4,5,6,7)
# sum=0
# my_lst=list(tpl)
# for num in my_lst:
#     sum=sum+num
# print(sum)
# for i in range(1,11):
#     for j in range(1,11):
#      print(i * j,end=" ")
#     print()

# name=input("enter your name : ")
# range=int(input("enter your range : "))
# for i in range(range,0,-1):
#    print((name + ' ')* i)

# for i in range(1,8):
#    for j in range(8-i):
#       print(i,end=" ")
#    print()
# name = input("Enter your name: ")
# range= int(input("Enter the range: "))

# # if range > len(name):
# #    range_val = len(name)

# for i in range(range):
#    for j in range()
   
# #
# name=input("enter your name : ")
# limit=int(input("enter your range : "))
# for i in range(limit):
#    print(name)
# n=8
# for i in range(1,n):
#    for j in range(n-i):
#       print(i,end=" ")
#    print()

# for num in range(10,51):
#    if num % 2 != 0 and num % 3 !=0: 
#       print(num)

# i=10
# while(i<=50):
#    if i % 2 != 0 and i % 3 !=0: 
#       print(i)
#    i+=1

# text=input("enter the palindrome : ")
# rev_text=reversed(text)
# if list(text)==list(rev_text):
#    print(f" the string {text} is a palindrome")
# else:
#    print(f" the string {text} is not a palindrome")




# string=input("Enter string : ")
# revstr =""
# for i in string:
#    revstr=i+revstr
# print(f"Reversed string is {revstr}")
# if(string == revstr):
#    print("The string is a palindrome.")
# else:
#  print("The string is not a palindrome.")



# print("Welcome to the electricity bill calcuator ....here we go : ")

# unit_consumed=float(input("enter the unit consumed : "))
# if unit_consumed<=100:
# 	total_bill=0
   
# elif unit_consumed<=200:
#     total_bill=float(unit_consumed)*5
# else:
#     total_bill=float(unit_consumed)*10
# print(f"your total electricity bill is {total_bill}")


# num1=int(input("enter number"))
# num2=int(input("enter number"))
# num3=int(input("enter number"))
# combination=[]
# combination.append(num1)
# combination.append(num2)
# combination.append(num3)

# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if(i!=j & j!=k & k!=i):
#                 print(combination[i],combination[j],combination[k])

    
n = 5

# Upper part of the pattern
# for i in range(n):
#     spaces = " " * (n - i - 1)
#     if i == 0:
#         print(spaces + "*")
#     else:
#         stars = " " * (2 * i - 1)
#         print(spaces + "*" + stars + "*")

# # Lower part of the pattern
# for i in range(n - 2, -1, -1):
#     spaces = " " * (n - i - 1)
#     if i == 0:
#         print(spaces + "*")
#     else:
#         stars = " " * (2 * i - 1)
#         print(spaces + "*" + stars + "*")



# from re import *
# text="kaBczabc 9@7c"
# pattern="[abc]"
# matcher=finditer(pattern,text)
# for m in matcher:
#    print(m.start(),m.group())





# dob dd-mm-yyyy
from re import *
DOB=input("enter date of birth dd-mm-yyyy")
rule="(0[1-9]|[12][0-9]|3[0-1])-(0[1-9]|1[0-2])-(19|20)[0-9]{2}"


# anagram
# kangrao
# paliondrome
# fibbanocci
# patterns
# valid paranthesis
# regular expresssion
