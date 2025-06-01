class Car:
    wheels = 5
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self,increment):
        self.speed += increment
        return f"{self.brand} {self.model} is now moving at {self.speed}km/h"
    
    def brake(self):
        self.speed = 0
        return f"{self.brand} {self.model} has stopped"
    
    def displayInfo(self):
        return f"Car: {self.brand} {self.model}, Wheels: {Car.wheels}, Speed: {self.speed} km/h"
        

Car1 = Car("Hyundai","verna")
print(Car1.accelerate(400))
print(Car1.displayInfo())
print(Car1.wheels)
print(Car1.model)