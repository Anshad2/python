
from abc import ABC,abstractmethod

class DbConnect(ABC):

    @abstractmethod
    def __init__(self,user,password,port,database):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass

class MyDb(DbConnect):

    def __init__(self, user, password, port, database):
        self.user=user
        self.password=password
        self.port=port
        self.database=database

    def connect(self):
        print("db Connection initiated....")

    def execute_query(self):
        print("db Executing query.....")

    def close(self):
        print("db Closing connection......")

obj=MyDb("Anshad","Password@132",2024,"mydb")
obj.connect()
obj.execute_query()
obj.close()