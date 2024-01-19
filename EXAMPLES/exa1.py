n=int(input("number"))
if n%2==0 and 2<n<5:
    print("Not Weird")
elif n%2==0 and 6<n<20:
    print("Weird")
elif n%2==0 and n >20:
    print("Not Weird")
else:
    print("Weird")

# // and /
num1=4
num2=3
print(num1//num2)#integer division
print(num1/num2)#float division


# 
num1=5
num2=6
add=num1+num2
print(f"{add}")


for i in range(1,5):
    print(i**2)