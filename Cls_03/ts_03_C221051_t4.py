# Function to calculate sum in tuple
def tupleOperations(numbers):
    # Initialize sum variable as 0
    sum_of_tuple = 0
    # use for loop to iterate over every numbers in tuple
    for number in numbers:
        sum_of_tuple+=number
        
    # Return sum value
    return sum_of_tuple

# Base function that will call in program start for user input and print 
def base():
    # Initialize the tuple with values
    numbers = (10, 20, 30, 40, 50)
    # Call sum calutation function for sum of tuple
    sum_of_numbers = tupleOperations(numbers)
    
    print("Sum of numbers in tuple : ", sum_of_numbers)
    
    # Trying to modify a value of tuple
    try:
        numbers[len(numbers)-1] = 100
        print("Changed last element to ",numbers[len(numbers)-1])
    except TypeError as e:
        print("Found Error : ",e)
        
base()