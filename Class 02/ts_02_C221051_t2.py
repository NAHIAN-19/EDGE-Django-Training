# Task - 1 : Nested conditions

# Take student mark as input
student_mark = int(input("\nEnter student mark : "))

# Check if student mark is greater than 40(Pass) or Fail
if student_mark > 40 and student_mark <= 100:
    # Check if student mark is greater than 80
    if student_mark >= 80:
        print("\nStudent Grade is : A\n")
        
    # Check if student mark is greater than 60
    elif student_mark >= 60:
        print("\nStudent Grade is : B\n")
        
    # Check if student mark is greater than 50
    elif student_mark > 40:
        print("\nStudent Grade is : C\n")
        
# If student mark is less than 40 then he/she fails
elif student_mark < 40 and student_mark >= 0:
    print("\nStudent Grade is : Fail\n")
    
else:
    print("\nInvalid mark entered\n")