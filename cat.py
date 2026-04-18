class Cat:
     def __init__(self,color,legs):
         self.color=color
         self.legs=legs
     def __str__(self):
        return 'cr'+self.color+','+str(self.legs)
    
pet1=Cat('ginger',4)
print(pet1.legs)
print(pet1.color)
print(pet1)

pet2=Cat('brown',3)
print(pet2.legs)
print(pet2.color)
print(pet2)
