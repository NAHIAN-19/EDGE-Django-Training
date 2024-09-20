# Module practice
from custom_modules.module_1 import calculateArea, celsiusToFarenHeit


# User Temperature input as Celsius
temp_in_celsius = float(input("Enter temperature in celsius : "))
# Call custom_module for celsius to farenheit conversion
print("Temeperature in Farenheit is : ",celsiusToFarenHeit(temp_in_celsius),"F\n")

# User Radius input 
radius_of_cicle = float(input("Enter Radius of circle : "))
# Call custom_module for area calculation 
print("Area of Circle is : ", calculateArea(radius_of_cicle))