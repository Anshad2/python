class Book:
    name:str
    author:str
    page:int
    price:int

    # instance variable self
    # initializing instance variable constractor
    # python __init__
    def __init__(self,name,author,page,price):
        self.name=name
        self.author=author
        self.page=page
        self.price=price

    def display_book(self):
        print(self.name,self.author,self.page,self.price)
    
    def __str__(self):
        return self.name


# object
obj=Book("harrypotter","jj scroll",800,499)
obj.display_book()
print(obj)



