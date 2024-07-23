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


def read_passwords(file_path='passwords.txt'):
    passwords = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if ': ' in line:
                    place, password = line.strip().split(': ', 1)
                    passwords[place] = password
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        pass
    return passwords


def write_passwords(passwords, file_path='passwords.txt'):
    with open(file_path, 'w') as file:
        for place, password in passwords.items():
            file.write(f"{place}: {password}\n")


def main():
    passwords = read_passwords()

    # Ask the user for input
    try:
        minimum_length = int(input("Enter the desired password length: "))
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Generate and print the password
        password = generate_password(minimum_length, include_numbers, include_special_chars)
        print(f"Generated password: {password}")

        # Prompt user to see if they like the password
        use_password = input("Do you like this password and would you like to use it? (yes/no): ").strip().lower()

        if use_password == 'yes':
            place = input("Where will you use this password? ").strip()
            passwords[place] = password
            write_passwords(passwords)
            print("Password stored successfully.")
        else:
            print("Password not stored.")

        # Ask the user if they want to update an existing password
        update_password = input("Do you want to update an existing password? (yes/no): ").strip().lower()
        if update_password == 'yes':
            place_to_update = input("Which place's password do you want to update? ").strip()
            if place_to_update in passwords:
                new_password = input(f"Enter the new password for {place_to_update}: ").strip()
                passwords[place_to_update] = new_password
                write_passwords(passwords)
                print(f"Password for {place_to_update} updated successfully.")
            else:
                print(f"No password stored for {place_to_update}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
