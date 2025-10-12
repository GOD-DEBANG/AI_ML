# Inharitance

class Parents: #Parent class (Super class)
    a = "I am Debang Chowdhury"

    def hello(self):
        print("Hello I am a method inside a factory")

class Parent(Parents): #Child Class (sub class)
    pass

obj = Parents

print(obj.a)

obj2 = Parent()

print(obj2.hello())



