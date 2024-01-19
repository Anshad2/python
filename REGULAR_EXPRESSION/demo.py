# for pattern matching eg:vehicle number dob(dd-mm-yyyy),pan card etc
# re module
# from re import *

# from re import *

# string="abababab"
# Pattern="ab"
# matcher=finditer(Pattern,string)
# for obj in matcher:
#     print(obj.start())
#     print(obj.group())

# 
# from re import *
# text="abchellowarsduyfguihello"
# matcher=finditer(Pattern,text)
# for m in matcher:
#     print(m.start(),m.group())
# to check email,password etc are correct

from re import *
text="fat-cat-run-fast-catch"
pattern="at"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)


