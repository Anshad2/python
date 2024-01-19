n1=int(input("number"))
n2=int(input("number"))
sm_num = n1 if n1<n2 else n2
i=1
hcf=1
while(i<=sm_num):
    if (n1%i==0 and n2%i==0):
        hcf=1
    i+=1
print(f"hcf of {n1} and {n2} = {hcf}")
lcm=(n1*n2)/hcf
print(f"lcm of {n1} and {n2} = {lcm}")
    

