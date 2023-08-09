import re


def email_validator(list_of_emails: str) -> list:
    while True:
        email = input("Enter email:  ")
        if not re.search(r'[a-z]', email):
            print("Invalid ")
        elif email.startswith('@'):
            print('Invalid email')
        elif email.count('@') > 1:
            print('Invalid email')
        elif email.__contains__('.',   ):
            print("Valid email")
        elif re.search(r'[0-9]', email):
            print("Invalid email")
        else:
            print('Valid email')


valid_email = ('@ashley.com', '423q', )
print(email_validator(valid_email))
# def is_email_valid(list_of_emails):
