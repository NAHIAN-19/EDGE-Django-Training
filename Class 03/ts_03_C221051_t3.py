def listOperations(number_list, size_of_list):
    
    # Initialize sum , max, min value with 0 & first value of list
    sum_of_total_list = 0
    largest_number = number_list[0]
    smallest_number = number_list[0]
    """
        Use for loop to iterate over every number for
        calculating sum, maximum & minimum number
    """
    for number in number_list:
        # Sum of all elements in the list
        sum_of_total_list += number
        # find largest number by getting the max value in every compare
        largest_number = max(largest_number, number)
        # Find minimum value by comparing minimum value and every numbers
        smallest_number = min(smallest_number, number)
        
    """
        Calculate average of the list by dividing sum of numbers
        in the list by size of list
    """
    average_of_list = sum_of_total_list/size_of_list 

    # Return the values found after operations
    return sum_of_total_list , largest_number, smallest_number, average_of_list

def base():
    # Enter the size of list
    size_of_list = int(input("Enter the number of elements for list : "))
    
    # Take list numbers from user
    number_list = []
    
    # Use for loop to take numbers in list 
    for number in range(size_of_list):
        user_input = int(input("Enter ",number,"st value : "))
        number_list.append(user_input)
        
    # Call the function to return the result after performing operations
    sum_of_total_list, largest_number, smallest_number, average_of_list = listOperations(number_list, size_of_list)
    
    print("\nSum of numbers in list : ",sum_of_total_list)
    print("\nMaximum Number : ",largest_number)
    print("\nMinimum Number : ",smallest_number)
    print("\nAverage of numbers in List : ",average_of_list)
    
base()