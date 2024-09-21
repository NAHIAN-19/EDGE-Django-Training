# Task : 1 - Create a class Person to get user info and geet the user
class Person:
    # Constructor to initialize the person object with name and age
    def __init__(self, user_name, user_age):
        # Initializing the name and age attributes
        self.name = user_name
        self.age = user_age

    # Method to display the information of the person
    def displayInfo(self):
        print(f"\nName : {self.name}\nAge : {self.age}\n")

    # Method to greeting to the person
    def greetUser(self):
        print(f"Hello {self.name}, you are {self.age} years old!")

# Take user input for their name and age
user_name = input("Please enter your name : ")
user_age = int(input("Please enter your age  : "))

# Creating an instance of the Person class with the user name and age
user_person = Person(user_name, user_age)
# Calling the displayInfo method to display the user information
user_person.displayInfo()
# Calling the greetUser method to greet the user
user_person.greetUser()
