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

    # Method to update the age of the person
    def updateAge(self, new_age):
        self.age = new_age
        print(f"\nUpdated age of {self.name} is {self.age} years old!")
        
# Take first user input for their name and age
user_name_1 = input("Please enter first person's name : ")
user_age_1 = int(input("Please enter first person's age  : "))

# Take second user input for their name and age
user_name_2 = input("\nPlease enter second person's name : ")
user_age_2 = int(input("Please enter second person's age  : "))

# Creating an instance of the first Person class with the user name and age
user_person_1 = Person(user_name_1, user_age_1)
# Calling the displayInfo method to display the user information
user_person_1.displayInfo()
# Calling the greetUser method to greet the user
user_person_1.greetUser()

# Creating an instance of the second Person class with the user name and age
user_person_2 = Person(user_name_2, user_age_2)
# Calling the displayInfo method to display the user information
user_person_2.displayInfo()
# Calling the greetUser method to greet the user
user_person_2.greetUser()


# Take the new age of the second user
new_age = int(input("\nPlease enter second person's new age : "))

# Updating the age of the second user
user_person_2.updateAge(new_age)

