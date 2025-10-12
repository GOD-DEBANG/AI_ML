# Types Of Inharitance


#Single inharitance


class parents:
    def __init__(self ,  skincolor , eyecolor , height , haircolor , personality , behavior ):
               self.skincolor = skincolor
               self.eyecolor = eyecolor
               self.height = height
               self.haircolor = haircolor
               self.personality = personality
               self.behavior = behavior
    def show(self):
        print(f"Skin Color: {self.skincolor}, Eye Color: {self.eyecolor}, "
                f"Height: {self.height}, Hair Color: {self.haircolor}, "
                f"Personality: {self.personality}, Behavior: {self.behavior}")
           

object = parents("Fair","Black","5.11","Black","Fair","Good")
object.show()

print(object) # Address of the object(Instance of Parents Class saved in the memory) 


        

# Multiple inharitence

class Animal:
   def __init__(self,name):
       self.name =name
   
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Robot(Animal,Human):
   def __init__(self, name , age , birthdate):
       self.name = name
       self.age = age
       self.birthdate = birthdate
       

obj = Human("Debang", 20)
obj2 = Animal("Kuswaha")
obj3  = Robot("Shriman",21,16122004)

print(obj.age)
print(obj2.name)
print(obj3.birthdate)




