# 1. Create a program to print all the numbers in the range 10-50 excluding the multiples of 2 and 3 
for num in range(10,51):
   if num % 2 != 0 and num % 3 !=0: 
      print(num)
# or
# i=10
# while(i<=50):
#    if i % 2 != 0 and i % 3 !=0: 
#       print(i)
#    i+=1

# 2. Python program to check if the given string is a palindrome.
string=input("Enter string : ")
revstr =""
for i in string:
   revstr=i+revstr
print(f"Reversed string is {revstr}")
if(string == revstr):
   print("The string is a palindrome.")
else:
 print("The string is not a palindrome.")

#  or
# word = input("please enter the word to check ")
# wrd_lst = []

# for w in word:
#     wrd_lst.append(w)

# new = wrd_lst.copy()
# new.reverse()

# for i in range(len(word)):
#     if new[i] != wrd_lst[i]:
#         print(f'{word} is not a palindrome.')
#         break
# else:
#     print(f'{word} is a palindrome.')

# or

# text=input("enter the palindrome : ")
# rev_text=reversed(text)
# if list(text)==list(rev_text):
#    print(f" the string {text} is a palindrome")
# else:
#    print(f" the string {text} is not a palindrome")
# 3. Pattern print 
#            1 1 1 1 1 1 1
#            2 2 2 2 2 2 2
#            3 3 3 3 3 3 3 
#            4 4 4 4 4 4 4
#            5 5 5 5 5 5 5


for i in range(1,6):
   for j in range(7):
      print(i,end=" ")
   print()