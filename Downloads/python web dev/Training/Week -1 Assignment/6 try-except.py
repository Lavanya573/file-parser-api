while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        print(f" You entered a valid integer: {number}")
        break  # Exit the loop if input is valid
    except ValueError:
        print(" Invalid input! Please enter an integer.")
