# amstron num= cube root of sum number is also the same  number
# length of string len() only for string
# 153=1cube + 5cube + 3 cube =153 which is called amstong number


num=input("enter the number")
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
print(sum)
print(f"{original} amstrong" if original==sum else "not amstrong")

    