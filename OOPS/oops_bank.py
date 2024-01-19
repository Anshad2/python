class Bank:
    acc_no:str
    name:str
    ac_type:str
    ifsc_code:str
    branch:str
    balance:int

    def creat_account(self, acc_no, name, ac_type, ifsc_code, branch, balance):
        self.acc_no = acc_no
        self.name = name
        self.ac_type = ac_type
        self.ifsc_code = ifsc_code
        self.branch = branch
        self.balance = balance

    def display_details(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.ac_type}")
        print(f"IFSC Code: {self.ifsc_code}")
        print(f"Branch: {self.branch}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print("your available balance is ",self.balance)

# object
acc1 =Bank()
acc1.creat_account("123456789", "anshad", "Savings", "ABC123", "Manj Branch", 8000)
acc1.display_details()
acc1.deposit(3500)
acc1.withdraw(6000)
acc1.withdraw(8000)
