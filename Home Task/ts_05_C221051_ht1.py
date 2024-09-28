# File Operations using SOLID Principles and OOP in Python

# For interacting with the operating system and clearing the console screen
import os
# For adding a delay to simulate user experience
import time
# For using the Abstract Base Class (ABC) and abstractmethod decorator
from abc import ABC, abstractmethod

""" 
    Abstract class to define file operations 
    enforcing SOLID principles like SRP and DIP
"""
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def append(self, data):
        pass

    @abstractmethod
    def delete(self):
        pass

""" 
    Concrete class for handling text files
    this makes sure we're adhering to Liskov Substitution (LSP)
"""
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    # Reads content from a file if it exists, otherwise throws an error
    def read(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"{self.filename} not found.")
        
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    # Overwrites the entire file content with new data
    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

    # Adds new content at the end of the file
    def append(self, data):
        with open(self.filename, 'a') as file:
            file.write(data)

    # Deletes the file if it exists
    def delete(self):
        if os.path.exists(self.filename):
            # Remove the file if it exists in the directory
            os.remove(self.filename)
            print(f"{self.filename} deleted successfully.")
        else:
            # Raise an exception if the file doesn't exist
            raise FileNotFoundError(f"{self.filename} not found.")

"""
    Manager class to interact with the file handler
    adheres to Dependency Inversion (DIP)
"""
class FileManager:
    def __init__(self, handler: FileHandler):
        self.handler = handler

    # Handles replacing the content of the file
    def write(self, data):
        print("Replacing/Overriding the file content...")
        # Simulating some delay for user experience
        time.sleep(1)
        self.handler.write(data)
        print("File content replaced successfully.")

    # Handles appending data to the file
    def append(self, data):
        print("Appending data to the file...")
        # Simulating some delay for user experience
        time.sleep(1) 
        self.handler.append(data)
        print("Data appended successfully.")

    # Reads the content of the file and prints it
    def read(self):
        try:
            print("Reading from file...")
            # Simulating some delay for user experience
            time.sleep(1)
            file_content = self.handler.read()
            print(f"\nFile content : \n\t{file_content}")
        # Catch the exception if the file doesn't exist
        except FileNotFoundError:
            print("File not found. Please add data to the file first.")

    # Deletes the file and handles any exceptions if the file doesn't exist
    def delete(self):
        try:
            print("Deleting file...")
            time.sleep(1)  # Simulating some delay here as well
            # Call the delete method of the file handler
            self.handler.delete()
        # Catch the exception if the file doesn't exist
        except FileNotFoundError:
            print("File not found. Nothing to delete.")


# Clears the console screen (works on both Windows and Unix-based systems)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu to interact with the user and perform file operations
def main_menu():
    print("Welcome to the File Manager!")
    """
        Prompt the user for the filename to manage, 
        defaulting to 'file_operations.txt' if no input is provided
    """
    filename = input("Enter the filename (Press Enter to skip): ").strip()
    
    # If the user presses enter without typing anything, set the default filename
    if not filename:
        filename = "file_operations"
    
    # Append '.txt' extension to the filename
    filename = f"{filename}.txt"
    # Create a TextFileHandler object to manage the file operations
    file_type_text = TextFileHandler(filename)
    # Create a FileManager object to interact with the file handler
    file_manager = FileManager(file_type_text)
    # Main loop to display the menu and handle user input
    while True:
        clear_screen()  # Clean the screen every time the menu is displayed
        print("=== File Manager Menu ===")
        print("1. Add (Append) to File")
        print("2. Replace/Override File Content")
        print("3. Read from File")
        print("4. Delete File")
        print("5. Exit")
        choice = input("Select an option: ")
        # Append data to the file
        if choice == '1':
            file_content = input("Enter data to add (append): ")
            file_manager.append(file_content)
            input("\nPress Enter to return to the menu...")  # Pause for user interaction
        # Replace the content of the file with new data
        elif choice == '2':
            file_content = input("Enter new content to replace the file content: ")
            file_manager.write(file_content)
            input("\nPress Enter to return to the menu...")  # Pause again
        # Read the content of the file and display it to the user
        elif choice == '3':
            file_manager.read()
            input("\nPress Enter to return to the menu...")  # Wait for user to review content
        # Delete the file if it exists
        elif choice == '4':
            # Confirm before deleting the file
            confirm = input("Are you sure you want to delete the file? (yes/no): ")
            if confirm.lower() == 'yes':
                file_manager.delete()
            else:
                print("Delete operation cancelled.")
            input("\nPress Enter to return to the menu...")  # Pause after deletion
        # Exit the program
        elif choice == '5':
            print("Exiting...")
            time.sleep(1)  # Graceful exit with a short delay
            break
        # Handle invalid input
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)  # Allow user to notice the error before refreshing the menu


# Entry point of the program
main_menu()

