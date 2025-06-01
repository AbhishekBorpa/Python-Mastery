class Animal:
    def __init__(self, name):
        self.name = name
    
    def speek(self):
        return f"{self.name} make a new sound"
    
    def eat(self):
        return f"{self.name} is eating"
    


class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def speek(self):
       return f"{self.name}, a {self.breed}, says Meow"
    
    def purr(self):
        return f"{self.name} is purring"
    

animal =  Animal("Normal Animal")
cat = Cat("Whisker","Persion")

print(cat.purr())