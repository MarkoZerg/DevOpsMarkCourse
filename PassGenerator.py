import string

import random

# Welcome message

print("Welcome, to password generator")


# Generate password with different characters
def generate_password(length):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation
    all_chars = lowercase+uppercase+letters+numbers+special  # Characters that need to be used

# Generate random password
    pas = ''.join(random.choice(all_chars) for _ in range(int(length)))

    return pas


# Password length
while True:
    password_length = input("Enter the desired password length (at least 6 characters): ")

    if int(password_length) >= 6:
        break  # Exit the loop if the password length is valid

    print("Requested password length is less than 6. Please try again.")


# Generate and show password to user
password = generate_password(int(password_length))
print("This is your secure password. Store it in a safe location:")
print(password)
