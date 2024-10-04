
# Write a script with 50 type conversation/string operation combined.

# using while loop to show a menu to switch between type conversion and string operations.
while True:
    # Show a menu to switch between type conversion ,string operations and exiting program.
    select_option = input("\n\t1. Type Conversion\n\t2. String Operations\n\t0. Exit\n\n\tSelect an option : ")

    # Show type conversion operations if selected option is 1
    if select_option == "1":

        # Type Convertion
        print("\n-- Type Convertions --\n\n")
        int_value = int(input("Enter a integer value : "))
        float_value = float(input("Enter a floating point value : "))
        string_value = input("Enter a string value(numbers) : ")
        boolean_value = bool(int(input("Enter a boolean value (1 for True, 0 for False) : ")))
        complex_value = complex(input("Enter a complex value (ex: 3+4j) : "))

        ##   Integer value conversions
        # Convert integer to float value
        int_to_float = float(int_value)

        # Convert integer to string value
        int_to_string = str(int_value)

        # Convert integer to boolean value
        int_to_boolean = bool(int_value)

        # Convert integer to complex value
        int_to_complex = complex(int_value)

        # Print converted different values
        print("\n\nConvert Integer value to different types\n")
        print("Integer to float : ", int_to_float)
        print("Integer to string : ", int_to_string)
        print("Integer to boolean : ", int_to_boolean)
        print("Integer to complex : ", int_to_complex)

        ##   Float value conversions
        # Convert float to integer value
        float_to_int = int(float_value)

        # Convert float to string value
        float_to_string = str(float_value)

        # Convert float to boolean value
        float_to_boolean = bool(float_value)

        # Convert float to complex value
        float_to_complex = complex(float_value)

        # Print converted different values
        print("\n\nConvert Float value to different types\n")
        print("Float to integer : ", float_to_int)
        print("Float to string : ", float_to_string)
        print("Float to boolean : ", float_to_boolean)
        print("Float to complex : ", float_to_complex)

        ##  String value conversions(numbers)
        #  Check if given string value is a number or not 
        if string_value.isalnum():
            
            # Convert string to integer value
            string_to_int = int(string_value)

            # Convert string to float value
            string_to_float = float(string_value)

            # Convert string to boolean value
            string_to_boolean = bool(string_value)

            # Convert string to complex value
            string_to_complex = complex(string_value)

            print("\n\nConvert String value to different types\n")
            print("String to integer : ", string_to_int)
            print("String to float : ", string_to_float)
            print("String to boolean : ", string_to_boolean)
            print("String to complex : ", string_to_complex)

        elif string_value.isalnum() is False:
            print("String convertion failed! Given string value is not a number!")
            

        ## Boolean value conversions
        # Convert boolean to integer
        boolean_to_int = int(boolean_value)

        # Convert boolean to float
        boolean_to_float = float(boolean_value)

        # Convert boolean to string
        boolean_to_string = str(boolean_value)

        # Convert boolean to complex
        boolean_to_complex = complex(boolean_value)

        print("\nConvert Boolean value to different types\n")
        print("Boolean to integer: ", boolean_to_int)
        print("Boolean to float: ", boolean_to_float)
        print("Boolean to string: ", boolean_to_string)
        print("Boolean to complex: ", boolean_to_complex)


        ## Complex value conversions
        # Convert complex to integer (using real part)
        complex_to_int = int(complex_value.real)

        # Convert complex to float (using real part)
        complex_to_float = float(complex_value.real)

        # Convert complex to string
        complex_to_string = str(complex_value)

        # Convert complex to boolean (using real part)
        complex_to_boolean = bool(complex_value.real)

        print("\nConvert Complex value to different types\n")
        print("Complex to integer (real part): ", complex_to_int)
        print("Complex to float (real part): ", complex_to_float)
        print("Complex to string: ", complex_to_string)
        print("Complex to boolean (real part): ", complex_to_boolean)

        # Take any key input to back to main menu
        input("\nPress any key to back to main menu...")

    # Show string operations if selected option is 2
    elif select_option == "2":

        # String Manipulations

        # Get Original string
        print("\n\t\tString Manipulations")
        original_string = input("\n\tEnter a string: ")

        # String conversion using different functions
        # Convert original string to uppercase
        original_to_upper = original_string.upper()

        # Convert original string to lowercase
        original_to_lowercase = original_string.lower()

        # Replace a part of original string with another string if it exists
        replace_original = original_string.replace("positive", "negative")

        # Check if a specific part exists in the original string, returns index or -1
        find_in_original = original_string.find("positive")

        # Fill total length of 30 with zero if string size is less than 30
        fill_original_with_zero = original_string.zfill(30)

        # Swap uppercase characters with lowercase and vice versa
        swapcase_original = original_string.swapcase()

        # Check if original string starts with "P"
        original_startswith = original_string.startswith("P")

        # Check if last character is "."
        original_endswith = original_string.endswith(".")

        # Remove beginning and ending whitespaces from original string
        stripped_original = original_string.strip()

        # Search for a specific part in the string, returns index or throws error
        search_in_original = original_string.index("o")

        # Check if all characters in string are alphanumeric (a-z, 0-9) or not
        alnum_original = original_string.isalnum()

        # Check if all characters in string are alphabet or not
        alpha_original = original_string.isalpha()

        # Check if all characters in string are ASCII characters or not
        ascii_original = original_string.isascii()

        # Check if all characters in string are digits or not
        numbers_original = original_string.isdigit()

        # Check if all characters in string are decimal numbers (0-9)
        decimal_original = original_string.isdecimal()

        # Check if the original string is an identifier (a-z, 0-9, _) or not
        identifier_original = original_string.isidentifier()

        # Check if the first character of each word is capitalized and the rest are small
        title_original = original_string.istitle()

        # Convert original string to title format
        original_to_title = original_string.title()

        # Add specific character in the string with specific width AFTER the string
        left_justify_original = original_string.ljust(30, "@")

        # Add specific character in the string with specific width BEFORE the string
        right_justify_string = original_string.rjust(30, "#")

        # Print results of all string manipulations
        print("\n--- String Manipulations Result---\n")

        print("Original string: ", original_string, "\n")
        print("Uppercase: ", original_to_upper)
        print("Lowercase: ", original_to_lowercase)
        print('Replace "positive" with "negative": ', replace_original)
        print('Find "positive" in string (index): ', find_in_original)
        print("Fill with zeros (30 length): ", fill_original_with_zero)
        print("Swapcase (upper/lower swap): ", swapcase_original)
        print("Starts with 'P': ", original_startswith)
        print("Ends with '.': ", original_endswith)
        print("Stripped (remove leading/trailing whitespaces): ", stripped_original)
        print('Index of "o": ', search_in_original)
        print("Is alphanumeric: ", alnum_original)
        print("Is alphabetic: ", alpha_original)
        print("Is ASCII: ", ascii_original)
        print("Is digit: ", numbers_original)
        print("Is decimal: ", decimal_original)
        print("Is identifier: ", identifier_original)
        print("Is title case: ", title_original)
        print("Title format: ", original_to_title)
        print('Left justify (width 30, fill "@"): ', left_justify_original)
        print('Right justify (width 30, fill "#"): ', right_justify_string)

        # Take any key input to back to main menu
        input("\nPress any key to back to main menu...")
        
    # Exit program if selected option is 0
    elif select_option == "0":
        print("Exiting program...")
        break
        
    # Show error message if selected option is invalid and continue the loop
    else:
        print("Invalid option selected! Please select a valid option (1 or 2 or 0).")
        continue