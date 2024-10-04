# List comprehension & lamda functions
def listComprehension():
    # Use list Comprehension to generate even numbers from 1 to 50
    a = 1
    b = 51
    even_numbers = [a for a in range(b) if a%2==0 ]
    # Use lambda function to multiply each even number by 3
    multiplied_even_numbers = list(map(lambda x: x *3 , even_numbers))
    print(multiplied_even_numbers)
    
listComprehension()