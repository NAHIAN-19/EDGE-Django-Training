# Parent class
class Vehicle:
    # Parent class constructor
    def __init__(self,model,year, wheels):
        self.model = model
        self.year = year
        self.wheels = wheels
    
    # Parent class method
    def start_engine(self):
        print(f"{self.model} built in {self.year} has {self.wheels} wheels\n")
    
# Child class inherits method and attributes from parent class
class Car(Vehicle):
    def __init__(self, model, year, wheels, doors):
        # Super class gets inherited attribute and methods from Parent class
        super().__init__(model, year, wheels)
        self.doors = doors
        
    # Child class speciailized method for Car class only
    def car_info(self):
        print(f"{self.model} built in {self.year} has {self.doors} doors and {self.wheels} wheels\n")

# Child class inherits method and attributes from parent class
class Bike(Vehicle):
    def __init__(self, model, year, wheels, cornering_angle):
        # Super class gets inherited attribute and methods from Parent class
        super().__init__(model, year, wheels)
        # Child class own attributes
        self.cornering_angle = cornering_angle
        
    # Child class speciailized method for Bike class only
    def bike_info(self):
        print(f"""{self.model} built in {self.year} has {self.wheels} wheels """,end="")
        print(f"""with {self.cornering_angle} degree cornering angle\n""")
        
# Create objects of Parent class
vehicle = Vehicle("Bugatti Veryon",2023, 4)

# Create objects of Child class
car = Car("Tesla",2021, 4, 2)
bike = Bike("Discover", 2015, 2, 25)

# Call own methods
vehicle.start_engine()

# Call Own & inherited methods
car.start_engine()
car.car_info()

# Call own and inherited methods
bike.start_engine()
bike.bike_info()