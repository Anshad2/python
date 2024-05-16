# defining the function to find the nth Fibonacci Number  
def Fibonacci_series(x):  
    # Taking First two terms of the Fibonacci Series as 0 and 1  
    fib_lst = [0, 1]  
    # Here, as we know that the first two terms of Fibonacci Series are 0 and 1,  
    # we append the remaining values (Fibonacci numbers from index 2 to x)  
    # in the array using recursion and return the last element.   
    # In the range function, we take range(2, x + 1) instead of range(2, x).  
    # This is because range function in python iterates until the value  
    # before the upper limit. So, if we take from 2 to x, it would only  
    # iterate from second to (x - 1)th element.  
    for n in range(2, x + 1):  
        fib_lst.append(fib_lst[n - 1] + fib_lst[n - 2])  
    return fib_lst[x]  
print("12th Term of Fibonacci Series:", Fibonacci_series(15))  

# remove white space strip() " hello world "

