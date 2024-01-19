from abc import ABC,abstractmethod

class Editor(ABC):


    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    
    def edit(self):
        print("edited")

    def debug(self):
        print("debuged")

    def execute(self):
        print("executed")

obj=Vscode()
obj.edit()