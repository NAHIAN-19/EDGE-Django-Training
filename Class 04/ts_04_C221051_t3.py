"""
    Car class to represent a car object with model and fuel efficiency
"""
class Car:
    # Constructor to initialize the car object with model and fuel efficiency
    def __init__(self, car_model, fuel_efficiency):
        self.model = car_model
        self.fuel_efficiency = fuel_efficiency

    # Method to drive the car
    def drive(self):
        print(f"\n{self.model} is being driven.")
"""
    FuelEfficiencyCalculator class to calculate the
    fuel efficiency based on miles driven and fuel consumed
"""
class FuelEfficiencyCalculator:
    def __init__(self, car):
        self.car = car

    def calculate_fuel_efficiency(self, miles_driven, fuel_consumed):
        return miles_driven / fuel_consumed

# Take user input for car model and fuel efficiency
car_name = input("Please enter the car model : ")
fuel_efficiency = int(input("Please enter the fuel efficiency of the car : "))
# Create a car object
car_info = Car(car_name, fuel_efficiency)

# Create a fuel efficiency calculator object
efficiency_calculator = FuelEfficiencyCalculator(car_info)


# Take user input for miles and fuel to calculate fuel efficiency
miles_driven = int(input("Please enter the number of miles driven : "))
fuel_consumed = int(input("Please enter the fuel consumed amount : "))

# Drive the car
car_info.drive()

fuel_efficiency = efficiency_calculator.calculate_fuel_efficiency(miles_driven, fuel_consumed)
print(f"\nThe fuel efficiency is {fuel_efficiency} miles per gallon.")
