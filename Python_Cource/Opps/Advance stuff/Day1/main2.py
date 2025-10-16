# Args and Kwargs

def add(a,b):
    print(a+b)
    return add

add(20,20)

# Using multiple arguments
# Using args , works in position form as a positional  based agguments

def add1(*args):
    sum = 0

    for i in args:
        sum = sum+i

        print(sum)

add1(20,20,10,20,40,50,70,70,80,80)


# Using keyword arguments

# Using kwargs , works in keywords form as a keywords based agguments

def addition(**kwargs):
   for i in kwargs:
       print(f"{i}: {kwargs[i]}")

addition(a=10,b=20,c=30,d=40)    


# In decorator

def addition(func):
    def wrapper(*args,**kwargs):
       print("I will print myself before hello")
       func(*args,**kwargs)
       print("I will print myself after")
    return wrapper 
  
@addition
def add(a,b,c,d,e,f,g,h,i):
    print(f"Addition of a and b is {a+b+c+d+e+f+g+h+i}")

add(20,30,20,40,50,70,80,90,100)


