import string
import random

# User Input: Prompt the user to specify the desired length of the password.
password_length = int(input("Enter the length of the password: "))

# Define the characters to be used in the password
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

# Combine all the characters into a list
password_characters = letters + digits + punctuation

# Generate a password by selecting a random character from the list for the specified length
password = ''.join(random.choice(password_characters) for i in range(password_length))

# Display the Password: Print the generated password on the screen.
print("Generated Password: ", password)