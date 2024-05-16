
# decorator
# Decorators are a powerful feature in Python that allow you to modify or extend the 
# behavior of functions or classes without directly modifying their code. They essentially wrap
#  another function and allow you to execute code before and after the wrapped function runs.


def swap_num(fn):#fn:sub 
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@swap_num
def smart_sub(n1,n2):
     return n1-n2

@swap_num
def div(n1,n2):
        return  n1/n2
print(smart_sub(2,10))
print(div(2,10)) 



def hello_decorators(fn):
     def wrapper(user):
          data="hello !"+ fn(user)
          return data
     return wrapper

@hello_decorators
def morning_greetings(user):
     return f"goodmorning {user}"
def afternoon_greetings(user):
     return f"goodafternoon {user}"
def evening_greetings(user):
     return f"good evening {user}"
print(morning_greetings("anshad"))
print(afternoon_greetings("anj"))
print(evening_greetings("resh"))




def b_decorators(fn):
     def wrapper():
        # data=f"<b>" + {fn()} + "<b>"
        # return data
        return "<b>" + fn() + "<b>"   
     return wrapper

@b_decorators
def get_hello():
     return "hello"
@b_decorators
def get_hai():
     return "hai"

print(get_hello())
print(get_hai())