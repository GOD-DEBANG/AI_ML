# Abstraction

from abc import ABC , abstractmethod #Importing Abstrct class method

class abstrct(ABC): # Importd Helper class(ABC)  # Abstract class
       @abstractmethod
       def perimeter(self):
           pass           # Abstrct method
       @abstractmethod
       def area(self):
           pass 

class square(abstrct): # Inhariting Abstract class
    def __init__(self,side):

        self.side = side

    def perimeter(self):
        print("Hello")

    def area(self):
        print("World")

class Circle(abstrct): # Inhariting Abstract class
    def __init__(self,radius):

        self.radius = radius

    def perimeter(self):
        print("Hello")

    def area(self):
        print("World")


obj = Circle(4)
obj2 = square(4)


