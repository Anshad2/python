def add_numbers(*args):
    return sum(args)

print(add_numbers(10,20))
print(add_numbers(10,20,30,40,50))

# * args(argumnets) = tuple
# (123,345,567,760,678) add last digit
def last_digit_sum(*args):
    last_digit=[n%10 for n in args]
    return sum(last_digit)
print(last_digit_sum(123,345,567,760,678))


# last digit sum
# 123,134,135,18,19
def last_digit_max(*args):
    digit=[n%10 for n in args]
    return max(digit)
print(last_digit_max(18,22,12,9))

# **kwargs =dictionary

def add_employee(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("salary"))
add_employee(id=10,name="hari",n_place="ekm",w_place="tvm",salary=60000)

# 
def last_digit_sort(*args,**kwargs):
    digits=[n%10 for n in args]
    value=kwargs.get("reveresed")
    if value==True:
        digits.sort(reverse=True)
    else:
        digits.sort()
    return digits
print(last_digit_sort(19,17,18,16,5,4))


