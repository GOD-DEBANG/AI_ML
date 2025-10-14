# Dunder method

class person():
    def __init__(self,name): # __init__ is the dunder method
        self.name = name
    # def show(self):  # If THis only written then the object address will get printed
    #     print("Hii")    

    def __str__(self): # if this dunder method not Written then the object location will print
        return f"Hello how are you{self.name}"
    
obj = person("Debang")

print(obj)
        