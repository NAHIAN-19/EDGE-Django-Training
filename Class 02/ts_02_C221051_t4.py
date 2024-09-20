# Task - 3 : Print Multiplication table of a given number using while loop

# Get the number from user
multiply_number = int(input("Enter the number to print multiplication table : "))

# Initialize the multiplier to start from 1 to 10
multiplier = 1

# Print the multiplication table of given number in form of 'number x multiplier = result'
while multiplier <= 10:
    print(multiply_number, 'x', multiplier, '=', multiply_number * multiplier)
    multiplier += 1