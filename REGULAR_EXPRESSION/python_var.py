from re import *

variable_name=input("enter the name")

rule="[a-zA-Z]{1}[a-zA-Z0-9_]*"# start with alphbet atleast 1 and lowercaSe and uppercase alphebet 
# numbers and_ any number so *

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher ==None else "valid" )


# Q:starting with k,l,m or n
# second place must be digit and that is divisible by 3
# follwed by any number of alphebhet and numbers

from  re import *
variable_name=input("enter the name")
rule="[k-nK-N]{1}[369]{1}[a-zA-Z0-9]*"
matcher=fullmatch(rule,variable_name)
print("invalid" if matcher==None else "valid")


