# {min,max} how many needed,* any count come or note come,(KL)fixed," " inbetween
# from re import *
# pan_number=input("enter your pan number")
# rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"

# matcher=fullmatch(rule,pan_number)
# print("invalid" if matcher==None else "valid")


# month 01-12
# |== or

# from re import *
# month=input("enter the month")
# rule="(0[1-9]|1[0-2])"
# matcher=fullmatch(rule,month)
# print("invalid" if matcher==None else "valid")


# date validate

# from re import *
# date=input("enter your date")
# rule="(0[1-9]|[12][0-9]|3[0-1])" # 0 and next one 0-9 or first 1 and next 0-9 or 2 first 0-9 second or 3 or 1-2
# matcher=fullmatch(rule,date)
# print("invalid" if matcher==None else "valid")

# year to validate 1900-2099
# from re import *
# year=input("year")
# rule="(0[1-9]|1[0-2]})"# first 19 or 20 and next two 0-9 {2 times}"(19|20)[0-9]{2})"
# matcher=fullmatch(rule,year)
# print("invalid" if matcher==None else "valid")

# dd-mm-yyyy



from re import *
DOB=input("enter dob in dd-mm-yyyy")
rule="(0[1-9]|[12][0-9]|3[0-1])-(0[1-9]|1[0-2])-(19|20)[0-9]{2}"
matcher=fullmatch(rule,DOB)
print("invalid" if matcher==None else "valid")