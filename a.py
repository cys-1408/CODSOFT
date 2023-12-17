import random
import string

def password(a):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(a):
        password += random.choice(characters)
    return password

def main():
    length = int(input("Enter the desired length of the password: "))

    if length > 0:
        generated_password = password(length)
        print("Generated Password:", generated_password)
    else:
        print("Please enter a valid positive integer length.")
main()
