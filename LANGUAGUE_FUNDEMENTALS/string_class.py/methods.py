# class str
# print is a function it is outside class, we can call direct... eg,print,input
# methods is define in class(plan),to call class we use   object.method name(),object means by using clss  
# what to creat called object
##1 casefold() = upper case to lowercae == advanced method
##2 capitalize = first letter to capital
##3 lower()=capital or capital case to lower case
##4 upper()= lower case to upper
##5 isalpha= true or false is true=full alphebet false mixed alphbet and number
##6 isdigit() = check total is number true= total number
##7 isalnum() = true =alphbet or number but not special chara
##8 strip() = we pass a chara to strip then that passed chara removed from left and right
##9 rstrip() = remove chara from right
##10 lstrip()= remove chara from left
##11 split() = to split words by ,
##13 startwith() = to check the word start with
##14 endswith()= to check end with
##15 count(" ")= count what we want count
##16 index()= position of specified letter            python enter
##17 join()=3124=3,1,2,4                                dir(str) enter  to check 
company="LUMINAR"
print(company.casefold())# casefold()

projector="django"
print(projector.capitalize())#capitalize()

course="PYTHON"
print(course.lower())#lower()

course="python"
print(course.upper())#upper()

company="12luminar"
print(company.isalpha())#isalpha()

company="1235"
print(company.isdigit())#isdigit()

company="123luminar"
print(company.isalnum())#isalnum

company="bbhellobb"
print(company.strip("b"))#strip("...")

company="hello cricket fotball"
print(company.split())#split()

text="pneumonoultramicroscopicsilicovolcanoconiosis"
print(text.startswith("pn"))#startwith()


text="pneumonoultramicroscopicsilicovolcanoconiosis"
print(text.endswith("is"))#endswith()

text="pneumonoultramicroscopicsilicovolcanoconiosis"
print(text.count("a"))#count(" ")

tex="pneumonoultramicroscopicsilicovolcanoconiosis"
print(text.index("sis"))#index()=specified position of passed word

text="313"
print(" ,".join(text))

