from re import *
f=open("C:\\Users\\user\\Desktop\\my python\\Regular_expression\\train_number.txt","r")
rule="[0-9]{5}"
for line in f:
    train_number=line.rstrip("\n")
    matcher=finditer(rule,train_number)
    for m in matcher:
       print(m.group())