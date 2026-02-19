import os
print("hellp world")
def clear_terminal():
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

# Usage:
input("enter")
clear_terminal()
print("This is a new print statement.")



