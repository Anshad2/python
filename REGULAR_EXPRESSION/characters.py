# from re import *

# text="kaBczabc 9@7c"
# pattern="[ac]"# a or c
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# # a or b or 
# from re import *
# text="kaBczabc 9@7c"
# pattern="[abc]"# a or b or c
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# for checking sequence "[a-e]"
# from re import *
# text="kaBczabc 9@7c"
# pattern="[a-e]"# a or b or c or d or e
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())


# UPPERCASE B

# from re import *
# text="kaBczabc 9@7c"
# pattern="[B]"# UPPER CASE"[B]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# a or b "[ab]"
# matches all  lower and upper[a-zA-Z]
# "[0-9]" check for all digits
# alphanumaric chara "[a-zA-Z0-9]"

# from re import *
# text="kaBczabc 9@7c"
# pattern="[a-zA-Z0-9]"#alphanumaric
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())



# exclude [^a-z]"

# from re import *
# text="kaBczabc 9@7c"
# pattern="[^a-z]" #exclude a-z
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())


# "[^a-zA-z0-9]" excluded
from re import *
text="kaBczabc 9@7c"# 8 th position is space
pattern="[^a-zA-Z0-9]"# exclude 
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

# 