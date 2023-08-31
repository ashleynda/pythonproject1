import re
import string


def password_validator():
    while True:
        password = input("Enter password:  ")
        if len(password) < 8:
            print("Make sure password is at least 8 or more characters")
        elif not re.search(r'[A-Z]', password):
            print("Make sure your password has at least a capital letter in it")
        elif not re.search(r'[a-z]', password):
            print("Make sure password has at least a small letter in it")
        elif not re.search(r'[0-9]', password):
            print("Make sure password has at least a digit in it")
        elif re.match('^[a-zA-Z0-9]*$', password):
            print("Make sure password has a special character")
        else:
            print("Valid password")
            print("Thank you")
            exit()
            return password_validator()


valid_password = password_validator()
print("Valid password", valid_password)