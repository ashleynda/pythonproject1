from tests.accountexceptions import InvalidAmountException, InsufficientAmountException


class Account:
    def __init__(self, account_number, account_name, pin):
        self.__balance = 0
        self.__account_name = account_name
        self.__account_number = account_number
        self.__pin = pin

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountException("Invalid amount")
        else:
            self.__balance += amount
        return self.__balance

    def getBalance(self, pin):
        if self.__validate_pin(pin):
            return self.__balance

    def withdraw(self, amount, pin):
        if amount > 0:
            self.__validate_pin(pin)
            self.amount_greater(amount)

            self.__balance -= amount
        else:
            raise InsufficientAmountException("OLE!!!!you no get money")

    def __validate_pin(self, pin):
        if self.__pin == pin:
            return True
        else:
            raise InsufficientAmountException("ya pin no dey correct, enter correct pin")

    def amount_greater(self, amount):
        if amount > self.__balance:
            raise InsufficientAmountException("Insufficient Fund")

    def get_account_name(self):
        return self.__account_name

    def get_account_number(self):
        return self.__account_number
