# Multileval Inharitance

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

    def show(self):
        print(f"The material of bag is {self.material} and no of zips is {self.zips} ")

class FactoryBhopal(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)

        self.color  =  color

    def show(self):
        print(f"The Material of the bag is {self.material} and no.of zips are {self.zips} and its color is {self.color}")

class Factorymumbai(FactoryBhopal):
    def __init__(self, material, zips, color , pockets):
        super().__init__(material, zips, color)

        self.pockets = pockets
    def show(self):
        print(f"The Material of the bag is {self.material} and no.of zips are {self.zips} and its color is {self.color} and the no of pockets is {self.pockets}")    


class Retailshop(Factorymumbai):
    def __init__(self, material, zips, color, pockets , price):
        super().__init__(material, zips, color, pockets)

        self.price = price

    def show(self):
        print(f"The Material of the bag is {self.material} and no.of zips are {self.zips} and its color is {self.color} and the no of pockets is {self.pockets} and its price is {self.price}")   


factory = Retailshop("Leather",4,"Black",4,12000)
factory.show()     
    

# HIrarchy Inharitance


class Parent:
    def __init__(self,haircolor , height , eyecolor , skincolor):
        self.haircolor = haircolor
        self.height = height
        self.eyecolor = eyecolor
        self.skincolor = skincolor

    def show(self):
        pass



class   Son(Parent):
    def __init__(self, haircolor, height, eyecolor, skincolor):
        super().__init__(haircolor, height, eyecolor, skincolor)

    def show(self):
        print(f"The haircolor of the son is{self.haircolor} and height is{self.height} , eyecolor is{self.eyecolor} skincolor is{self.skincolor} ")

    
class Daughter(Parent):
    def __init__(self, haircolor, height, eyecolor, skincolor):
        super().__init__(haircolor, height, eyecolor, skincolor)

    def show(self):
        print(f"The haircolor of the Daughter is{self.haircolor} and height is{self.height} , eyecolor is{self.eyecolor} skincolor is{self.skincolor} ")
           

son = Son("Black",5,"Black","Fair") 
son.show()


daughter = Daughter("Black",5,"Black","Fair")
daughter.show()