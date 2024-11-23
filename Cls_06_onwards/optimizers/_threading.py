# Single threading
from threading import Thread

def print_numbers():
    for i in range(1, 11):
        print(i)
        
def single_theading():
    thread = Thread(target=print_numbers)
    thread.start()
    thread.join()

# Multi threading
from multiprocessing import Process

def print_squares(numbers):
    for number in numbers:
        print(f"Square of {number} is {number ** 2}")
        
def print_cubes(numbers):
    for number in numbers:
        print(f"Cube of {number} is {number ** 3}")
        
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    process1 = Process(target=print_squares, args=(numbers,))
    process2 = Process(target=print_cubes, args=(numbers,))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print("Done!")
