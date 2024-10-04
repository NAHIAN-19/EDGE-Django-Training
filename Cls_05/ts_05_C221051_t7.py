# SOLID - Interface segregation principle
class Vehicle:
    pass

class Drivable(Vehicle):
    pass
        
class Flyable(Vehicle):
    pass
        
class Car(Drivable):
    def __init__(self, model = "Tesla"):
        self._model = model
        
    def drive(self):
        print(f"{self._model} is driving\n")
        
class Aeroplane(Flyable):
    def __init__(self, model = "Boing 77"):
        self._model = model
        
    def fly(self):
        print(f"{self._model} is flying\n")
        