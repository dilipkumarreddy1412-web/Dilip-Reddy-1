class Animal:
    price=500
    def __init__(self,name,color):
      self.name=name
      self.color=color
    def bark(self):
        print("grrr.......")
class Dog(Animal):
    
    def bark1(self):
        print("woof")
pet1=Dog("tomy","brown")
pet1.bark()
pet1.bark1()
print(pet1.name,"is of color",pet1.color,pet1.price)
 
