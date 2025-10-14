# Polymorphisamn
# Mthod over ridding , as human class show method has over ride the animal clas show method as object will class the subclass insted of parent class
class Animal:
    def show(self):
        print("Hello")  # Mthod Over ridding Only Works with inharitance

class Human(Animal):
    def show(self):
        print("How are you")

obj = Human()
obj.show()              


# Method overloading is not accepted in python

# Duck Typing
class Human:
    def show(self):
        print("My Name is Debang_Chowdhury")

class Human2:
    def show(self):
        print("My name is Debang_Kuswaha")

object1 = Human()
object1.show()

object2 = Human2()
object2.show()

