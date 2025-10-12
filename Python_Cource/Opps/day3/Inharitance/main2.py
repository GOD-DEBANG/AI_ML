#Constructor in inharitence



class Animal:
    def __init__(self,name):
        self.name = name


    def show(self):
        print(f"Hello My Name Is {self.name}")
        
class Human(Animal):
    def __init__(self, name , age):
        super().__init__(name)
        self.age = age

    def show(self):
       print(f"Hello My Nmae is {self.name} And My Age Is {self.age}")


animal1 = Animal("LION")
animal1.show()
persons = Human("Debang_Kuswaha",21) 
persons.show()       



person = Animal("Debang_Chowdhury") # Instance of Your Main Class

person.show()

person1 = Human("Debang_Kuswaha",21) # Instance Of Your Child Class

person1.show()


