# Ask user to input a number in string form
user_input = input("Enter a number (as a string): ")

try:
    # Try converting the string to an integer
    number = int(user_input)
    print(f" You entered the integer: {number}")
except ValueError:
    # If conversion fails, handle the error
    print(" Error: That is not a valid integer.")
print(type(user_input))     # before conversion
print(type(number))         # after conversion
