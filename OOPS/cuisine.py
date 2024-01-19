class Cuisine:
    name:str

    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    
class Dish(Cuisine):
    dish_name=str
    incr=str
    price=int

    def __init__(self,name,dish_name,incr,price):
        super().__init__(name)
        self.dish_name=dish_name
        self.incr=incr
        self.price=price

# object
obj1=Dish("chinees","chicken_soup","chicken",499)
print(obj1)
dis_obj2=Dish("southindian","masala dosa","potato",199)
print(dis_obj2)


    

# 

class Parent:
    def properties(self):
        self.vehicle=["bajaj","honda","splender"]
        return self.vehicle
    
class Child(Parent):
    def properties(self):

        self.context=super().properties()
        self.context.append("nano")
        return self.context
    
obj=Child()
print(obj.properties())



    