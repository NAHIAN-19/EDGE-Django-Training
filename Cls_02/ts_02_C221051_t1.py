# Task - 1 : Conditions

# Take 1 input from user
random_number = int(input("Enter a random number : "))

# Check if entered number is positive
if random_number > 0:
    print("\nEntered number is positive")
    
# Check if entered number is negative
elif random_number < 0:
    print("\nEntered number is negative")
    
# So if entered number is not positive or negative, then it should be zero
else:
    print("\nEntered number is zero")