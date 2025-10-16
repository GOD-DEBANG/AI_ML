
# Lamda Function

# Normal Form of addition using Function

def addition(a,b):
    print(a+b)

addition(20,20)    


# By using Lmada Function

add = lambda c,d:c+d

obj = add(50,50)

print(obj)


# Map Filter And Zips

# Map

a =[1,2,3,4,5,6,7,8,9,10]

result = map(lambda x : x*2,a)

obj1 = list(result) # Recomanded to convert object to list to show the information if not then it will show the object place

print(obj1)


# Filter
# Filter works on true and false
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

ab = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

result1 = filter(even,ab)

obj2 = list(result1)

print(obj2)


