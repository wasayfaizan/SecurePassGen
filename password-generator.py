import random
import string


def generate_password(minimum_length, numbers=True, special_characters=True):
    if minimum_length < 1:
        raise ValueError("Minimum length must be at least 1")

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    # Ensure the password meets the minimum length requirement
    password = []

    # Add at least one letter
    password.append(random.choice(letters))

    # Add at least one digit if numbers are enabled
    if numbers:
        password.append(random.choice(digits))

    # Add at least one special character if special characters are enabled
    if special_characters:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random choices from the allowed characters
    while len(password) < minimum_length:
        password.append(random.choice(characters))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Ask the user for input
try:
    minimum_length = int(input("Enter the desired password length: "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    # Generate and print the password
    print(generate_password(minimum_length, include_numbers, include_special_chars))
except ValueError as e:
    print(f"Error: {e}")
