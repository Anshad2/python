# def fnunction_name(parameter):
#    
def my_add(n1,n2):
    res=n1+n2
    return res# return value not printed
print(my_add(100,200))

# 
def my_cube(num):#defining the function with his name
    res=num**3# parameter 
    return res#final result is call by retun not here pritnting
print(my_cube(3))#if we want print

# sub
def my_sub(n1,n2):
    res=n1-n2
    return res
print(my_sub(10,8))

# multplication

def my_mul(n1,n2):
    res=n1*n2
    return res
print(my_mul(10,5))

# division
def my_div(n1,n2):
    res=n1/n2
    return res
print(my_div(10,5))




# 
def smart_sub(n1,n2):
    res=n1-n2 if n1> n2 else n2-n1
    return res

print(smart_sub(5,10))
# 

def cube(num=2):
    resu= num**3
    return resu
print(cube(4))# if 4 not passed then cube of 2 find.... if passed 4 num=2 replaced by passed value 4


# nth root num
def nth_power(num,n):# if n=2 then defult take squre # print(nth_power(10))
    resu=num**n
    return resu
print(nth_power(5,3))


def smallest_num(n1,n2):
    res=n1 if n1<n2 else n2
    return res
print(smallest_num(4,8))

# 
def oneth_digit_smallest_num(n1,n2):
    a=n1%10
    b=n2%10
    if a<b:
        return n2
        
    else: 
        return n1
print(oneth_digit_smallest_num(432,18))


