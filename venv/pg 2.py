import random
import string

def generate_password(minimum_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    print(letters, digits, special_character)

generate_password(10)
