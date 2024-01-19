# abstarction : implementaion details hide

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def __init__(self,name,brand,model):
        pass


    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):
    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model

    def start(self):
        print("swift starts")

    def accelerate(self):
        print("swift accelerate")

    def stop(self):
        print("swift stop")

obj=Swift("swift","maruthi",2024)
obj.start()