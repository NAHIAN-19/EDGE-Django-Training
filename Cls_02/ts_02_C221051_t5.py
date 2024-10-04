# Task - 3 : Practice of break and continue statements
# Take number for user for multiplication table
multiply_number = int(input("Enter the number for multiplication table: "))

# Skips the multiple of 3 between 1 to 10
for number in range(1, 11):
    # Check if the current number is divisible by 3
    if number % 3 == 0:
        continue # skip if current number is divisible by 3
    
    print(f"{multiply_number} * {number} = {multiply_number * number}") # print the multiplication table

