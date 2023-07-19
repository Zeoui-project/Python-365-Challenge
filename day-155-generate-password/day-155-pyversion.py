# %%
import random
import string

def generate_password(length):
    # Define the character pool for the password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range (length))

    # Return the generated password
    return password

# Prompt the user to enter the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Generate the password using the specified length
generated_password = generate_password(password_length)

# Print the generated password
print("Generated Password: ", generated_password)