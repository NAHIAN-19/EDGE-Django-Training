# Error Handing
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division by zero is not allowed'
    except TypeError:
        return 'Only numbers are allowed'
    
# user Input
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

# Function Call
result = divide(number1, number2)
print('Result:', result)