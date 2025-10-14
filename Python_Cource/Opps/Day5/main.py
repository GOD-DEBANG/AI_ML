# Encapsulation

#Public Attribute method
class Factory:
    a = "Pune"
    def show(self):
        print("Hello World")


object  = Factory()
object.show()
print(object.a)


# Protected Attribute method


class Factory:
    _a = "Pune" # Protected Classes
    def show(self):
        print("Hello World")

class Bhopal(Factory):
    def show(self):
        print(super()._a)

object2  = Bhopal()
object2.show()


# Private protected method

class Perents:
    __ab = "HELLO"
    def show(self):
       pass
class child(Perents):
     def show(self):
         print(super.__a) #Cant Access the information

obj = child()
obj.show()