from re import *

number=input("enter your mobile number")

rule="([+]91)(-)?[0-9]{10}"
matcher=fullmatch(rule,number)
print("invalid" if matcher==None else "valid")