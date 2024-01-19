# class:(plan)design pattern,or blueprint(1 atributs:functionality 2 methods:creating function)
#  a class is a blueprint for creating objects.
# object:()real world entity,It's a specific entity created from a class and holds
#  the values for the attributes defined in the class. Objects can access the methods
#  and properties defined in their class.



class Employee:
    id:int
    name:str
    department:str
    salary:int
    def set_emp(self,id,name,dep,sal):
        self.id=id
        self.name=name
        self.department=dep
        self.salary=sal

# self:point to current object

    def display_emp(self):
        print(self.id, self.name,self.department,self.salary)


 #object 
emp1=Employee()
emp1.set_emp(1234,"ram","hr",60000)

emp2=Employee()
emp2.set_emp(2287,"ans","soft",70000)

emp1.display_emp()
emp2.display_emp()




class Student:
    name:str
    rolno:int
    stream:str
    fees:int

    def set_student(self,name,rol,stream,fees):
        self.name=name
        self.rolno=rol
        self.stream=stream
        self.fees=fees
    
    def display_stud(self):
        print(self.name,self.rolno,self.stream,self.fees)

st1=Student()
print()
st1.set_student("anshad",3344,"ece",30000)
st1.display_stud()


# class BankAccount:
#     def __init__(self, acc_no, name, ac_type, ifsc_code, branch, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.ac_type = ac_type
#         self.ifsc_code = ifsc_code
#         self.branch = branch
#         self.balance = balance

#     def display_details(self):
#         print(f"Account Number: {self.acc_no}")
#         print(f"Name: {self.name}")
#         print(f"Account Type: {self.ac_type}")
#         print(f"IFSC Code: {self.ifsc_code}")
#         print(f"Branch: {self.branch}")
#         print(f"Balance: {self.balance}")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.balance}")
#         else:
#             print("Insufficient funds")

# # Example usage:
# acc1 = BankAccount("123456789", "John Doe", "Savings", "ABC123", "Main Branch", 5000)
# acc1.display_details()
# acc1.deposit(1500)
# acc1.withdraw(2000)
# acc1.withdraw(5000)


