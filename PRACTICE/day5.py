# 1.Write a python program to find factorial of a prime number
num=int(input("enter your number"))
is_prime=True
for i in range(2,num):
    if num % i ==0:
        is_prime=False
        break
if is_prime:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"it is a prime number and its factorial is {fact}")
else:
    print("the given number is not a prime")



# 2.Write a python program to display Fibonacci series and specify that number odd or even


def fibbanocci(n):
    pre_num = 0
    curr_num = 1
    fibbanocci_seq=[pre_num,curr_num]

    for i in range(2,n):
        next_num=pre_num+curr_num
        pre_num=curr_num
        curr_num=next_num
        fibbanocci_seq.append(next_num)
    return fibbanocci_seq
fibbanocci_num=fibbanocci(14)
print(fibbanocci_num)
for num in fibbanocci_num:
    if num  == 0:
     print(f"{num} is zero")
    elif num %2== 0 :
       print(f"{num} is even")
    else:
       print(f"{num} is odd")



# 3.Write a python program to reverse digits in a number
# eg 5678
# reverse 8765

num=int(input("enter the number"))
reversed_num = 0
while num != 0:# loop that continue until num become zero
    digit = num % 10# get last digit
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print(f" the Reversed Number is {reversed_num}")





def fibbanocci(n):
    pre_num=0
    curr_num=1
    fibbanocci_num=[pre_num,curr_num]

    for i in range(2,n):
        next=pre_num+curr_num
        pre_num=curr_num
        curr_num=next
        fibbanocci_num.append(next)
        return fibbanocci_num

fibbanocci_num=fibbanocci(6)
print(fibbanocci_num)


