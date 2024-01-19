# prime number
num=int(input("enter the number"))#1 and num is not consider
is_prime=True
for i in range(2,num):#range from 2 to num-1 
    if num%i==0:#i=2,3,4,..num-1
        is_prime=False
        break
print(is_prime)



# def prime_checker(num):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#     if is_prime:
#         print("is a prime")
#     else:
#         print("not a prime")
# prime_checker(10)













