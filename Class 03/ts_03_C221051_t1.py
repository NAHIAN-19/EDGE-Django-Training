# Task - 1 : Find Factorial of a number

# A function to calculate the factorial and return the final value
def generate_factorial(factor_value):
    factor_result = 1
    # Check if the value is greater than 0 or not
    if factor_value < 1:
        return 0
    # Use for loop to multiply value with value+1 until value is equal to factor value
    for value in range(1,factor_value+1):
        factor_result *= value
        
    # Return the factorial of factor_value
    return factor_result

# Function to get user input for calculating factorial and show the return result
def home():
    # Take user input for calculating factorial
    factor_value = int(input("Enter a numebr to find factorial : "))
    
    # Call factorial function to calculate and return result
    factor_result = generate_factorial(factor_value)
    
    # Check if the result is 0 or not
    if factor_result == 0:
        print(f"Invalid input!\n")
        return
    # print the factorial of the number
    print(f"Factorial of {factor_value} is : {factor_result}\n",)
    
    
# Call the input function when the program starts
home()