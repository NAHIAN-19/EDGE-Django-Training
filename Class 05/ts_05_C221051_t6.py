# Base class has specific behaivour that child class
# class Bird:
#     def fly(self):
#         print("Flying\n")
        
# class Sparrow(Bird):
#     pass

# class Penguin(Bird):
#     def fly(self):
#         # voilets LSP
#         raise Exception("Penguins can't fly\n")
    
###   Solution according to Liskov Substitution principle

# Base class has specific behaivour that child class inherits
class Bird:
    pass # No need to declare behaivours on base class

# Child class with specific behaivour from base class  
class FlyingBird(Bird):
    def fly(self):
        print("Flying\n")
    
# Child class that uses specific behaivour from base class
class Sparrow(FlyingBird):
    pass

# Child class with exectional behaivour inherits from base class
class Penguin(Bird):
    pass

