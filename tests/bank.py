from tests.account import Account
from tests.bankexceptions import NonExistentAccount, AmountNotEnoughException


class Bank:
    def __init__(self):
        self.__accounts = []

    def register(self, firstname: str, lastname: str, pin: str):
        name = f'{firstname} {lastname}'
        account = Account(self.__generate_account_number(), name, pin)
        self.__accounts.append(account)

    def find_account(self, account_number: str):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        raise NonExistentAccount('Account no dey')

    def __generate_account_number(self):
        return str(len(self.__accounts) + 1)

    def deposit(self, amount, account_number):
        self.find_account(account_number).deposit(amount)

    def checkBalance(self, account_number, pin):
        return self.find_account(account_number).getBalance(pin)

    def withdraw(self,account_number, amount, pin):
        self.find_account(account_number).withdraw(amount,pin)

