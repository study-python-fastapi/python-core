class Animal:
    def __init__(self,name,species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print(f"Making {self.name}'s sound")
        print(self.__dict__)

Animal1 = Animal("dog","special",8)
Animal1.make_sound()

Animal2 = Animal("snake","anaconda",4)
Animal2.make_sound()