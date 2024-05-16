# slicing concept
    # 012345678
name="TECHNOLAB"
#            -1

# print(name[1]) #[start:stop:step]
print(name[2:4])# up to stop-1 print
print(name[2:])
# print(name[:7])
print(name[6:])

# negative indexing
print(name[-1:-4:-1])
print(name[:-5:-1])

# to reverse a string [::-1]
print(name[::-2])

# check paliondrome
name="madam"
reversed=(name[::-1])# no start no end only step
print("paliondrom" if reversed==name else "not a palindrome")


string1="hello"
string2="goodmorning"

leng_string1=len(string1)
print(leng_string1)

rem=string2[leng_string1:]
print(rem)


# merging

string1='abc'
string2='def'
result=''
for i in range(0,len(string1)):
    out=string1[i] + string2[i]
    result+=out
print(result)



# 

srting1=input("enter string 1 : ")
string2=input("enter string 2 : ")

smallest_length=min(len(string1),len(string2))
result=""
for i in range(0,smallest_length):
    out= string1[i] + string2[i]
    result+=out

# slicing
if len(string1) > len(string2):
    rem=string1[smallest_length:]

else:
    rem=string2[smallest_length]

result+=rem
print(result)







x=input("enter 1 : ")
y=input("enter 2 : ")

min_len=min(len(x),len(y))
result=""
for i in range(0,min_len):
    out= x[i] + y[i]
    result+=out

if len(x)> len(y):
    rem=x[min_len]
else:
    rem=y[min_len]
result+=rem
print(result)


