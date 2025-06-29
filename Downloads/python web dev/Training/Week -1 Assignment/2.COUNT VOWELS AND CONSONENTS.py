#count vowels and consonents
# Get input from the user
input_string = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Iterate through each character in the string
for char in input_string:
    # Check if the character is an alphabet letter
    if char.isalpha():
        # Check if it's a vowel
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
