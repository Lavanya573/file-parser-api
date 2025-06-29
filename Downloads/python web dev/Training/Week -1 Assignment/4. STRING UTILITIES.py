#string utilities
# Simulating string_utils/string_operations.py
def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def string_length(s):
    return len(s)

# Simulating string_utils/string_validations.py
def is_palindrome(s):
    s_clean = ''.join(filter(str.isalnum, s.lower()))
    return s_clean == s_clean[::-1]

def is_alpha(s):
    return s.isalpha()

# Simulating main_program.py
def main():
    user_input = input("Enter a string: ")

    print("\n--- String Operations ---")
    print("Reversed:", reverse_string(user_input))
    print("Uppercase:", to_uppercase(user_input))
    print("Length:", string_length(user_input))

    print("\n--- String Validations ---")
    print("Is Palindrome?", is_palindrome(user_input))
    print("Contains only alphabetic characters?", is_alpha(user_input))

if __name__ == "__main__":
    main()
