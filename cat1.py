class Animal:
    def __init__(self,name,color):
      self.name=name
      self.color=color
class Dog(Animal):
    def bark(self):
        print("Woof")
class Cat(Animal):
    def mew(self):
        print("cat meow")
pet1=Dog("tomy","brown")
print(pet1.name)
pet1.bark()
pet2=Cat("lucky","white")
pet2.mew()
print(pet2.name)
