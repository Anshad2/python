# hcf of 2 nunmber
n1=int(input("what is your number"))
n2=int(input("what is you number"))

smallest_num=n1 if n1<n2 else n2 #find smallest among n1 and n2
fact=1#last final value store
i=1
while(i<=smallest_num):
    if (n1%i==0 and n2%i==0):
        fact=i
    i+=1
print(fact)





# 
n1=int(input("what is your number"))
n2=int(input("what is you number"))

