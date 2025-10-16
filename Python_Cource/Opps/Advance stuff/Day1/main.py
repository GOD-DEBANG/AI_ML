# Decorator



def decorate(func): # Creating Decorator Function ,Its totally upto you for giving the name of the decorator
    def wrapper():
        print("I will print myself before hello")
        func()
        print("I will print myself after")
    return wrapper

@decorate #  the name of the decorator should be same as name of the decorator function
def hello():
    print("Hello I am Debang_Chowdhury")


hello()


# Adding with decorators


def addition(func):
    def wrapper(a,b):
       print("I will print myself before hello")
       func(a,b)
       print("I will print myself after")
    return wrapper 
  
@addition
def add(a,b):
    print(f"Addition of a and b is {a+b}")

add(20,30)

