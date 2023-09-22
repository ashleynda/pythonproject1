import re

from bank import *
from tests.bankmainexception import *


def validate_name(name):
    if re.fullmatch("^[A-z]+[a-zs]+$", name):
        return
    raise IncorrectNameException("Wrong name")


def validate_pin(pin):
    if re.fullmatch("\\d{4}", pin):
        return
    raise IncorrectPinException("Wrong Pin")


# class ATM:
#     def __init__(self):
#         self.bank = Bank()
#
#     def main(self):
#         self.welcome()
#
#     def welcome(self):
#         print("""
#         Welcome to Guaranty Trust Bank
#         click:
#         1. Register Account
#         2. Transactions
#         3. Exit""")
#
#     # option = input("Enter option:  ")
#     # if option == "1":
#     #     self.bank
#     # elif option == "2":
#     #     self.main()
#     # elif option == "3":
#     #     self.exit()

def main(self=None):

    print("""
        Welcome to Guaranty Trust Bank
        click:
        1. Register Account
        2. Transactions
        3. Exit""")

    option = input("Enter option:  ")
    if option == "1":
        self.bank.register()
    elif option == "2":
        self.main()
    elif option == "3":
        self.exit()

    try:
        option_first_name= input("Enter your first name:  ")
        validate_name(option_first_name)

        option_last_name= input("Enter your last name:  ")
        validate_name(option_last_name)
    # name = input("Enter your name: ")
    # b1 = Bank()
    # b1.register(name)

main()