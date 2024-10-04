# Dictionary operations to access values for find sum,max,min
def dictionaryOperations(student_marks, total_num_of_students):
    sum_of_student_marks = 0
    # To access the value of every key values() func is used
    hightest_mark =max(student_marks.values())
    lowest_mark = min(student_marks.values())
    # Find average using values func to get scores/length of dic
    average_of_student_marks = sum(student_marks.values())/total_num_of_students
    
    return average_of_student_marks, hightest_mark, lowest_mark

def home():
    # User input for total number of students
    total_num_of_students = int(input("Enter total number of students : "))
    
    # Initialize empty dictionay to store student info with name and marks
    student_info = {}
    # Take student info(name, marks) as input and store them in dictionary
    for _ in range(total_num_of_students):
        
        student_name = input("Enter student name : ")
        student_mark = int(input(f"Enter {student_name}'s mark : "))
        # Set marks for student name in dictionary
        student_info[student_name] = student_mark\
    # Call function to get avg, min, max marks within student info
    average_of_student_marks, highest_mark, lowest_mark = dictionaryOperations(student_info, total_num_of_students)
    
    # Print student marks operations
    print("Average marks of students : ",average_of_student_marks)
    print("Highest Mark : ", highest_mark)
    print("Lowest Mark : ", lowest_mark)
    
# Run base function in program start for user input and calling other functions
home()