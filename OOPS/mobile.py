class Mobile:
    name:str
    brand:str
    price:int
    display:str
    
    def __init__(self,name,brand,display,price):
        self.name=name
        self.brand=brand
        self.price=price
        self.display=display
    
    def display_mobile(self):
        print(self.name,self.brand,self.display,self.price)

    def __str__(self):
        return self.name
# object
obj=Mobile("samsung","s16","amoled",39999)
obj1=Mobile("iphonepromax","apple","amoled",139999)
obj.display_mobile()
obj1.display_mobile()
print(obj)
print(obj1)

# to print(obj) we give
# def __str__(self):
#   return self.name