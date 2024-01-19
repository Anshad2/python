num=123
sum=0
while(num!=0):
    last_digit=num%10 # 123/10 = 3
    print(last_digit)
    sum=sum+last_digit # 3+last_digit
    num=num//10 # flooring 12.3//12
print(f"sum is {sum}")


# amstrong number (cube sum)
num=153
sum=0
while(num!=0):
    digit=num%10
    print(digit)
    cube=digit**3
    sum=sum+cube
    num=num//10
print(f"sum is {sum}")