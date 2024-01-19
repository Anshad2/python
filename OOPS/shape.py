class Shape:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

class Rectangle(Shape):
    def __init__(self, name,length,breadth):
        super().__init__(name)
        self.length=length
        self.breadth=breadth
    
    def area(self):
        result=self.length * self. breadth
        print(result)

class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        result=self.radius**2 * 3.14
        print(result)

# object
rec_obj=Rectangle("rectangle",8,5)
rec_obj.area()
print(rec_obj)

cir_obj=Circle("circle",5)
cir_obj.area()
print(cir_obj)