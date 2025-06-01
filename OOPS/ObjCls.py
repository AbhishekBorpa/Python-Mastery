class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof Woof"
    
    def walk(self):
        return f"{self.name} is {self.age} years old"
    

dog1 = Dog("Chubby",3)
print(dog1.age)