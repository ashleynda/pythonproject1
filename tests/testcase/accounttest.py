import unittest
from tests.account import Account
from tests.accountexceptions import InvalidAmountException, InsufficientAmountException


def getBalance():
    pass


class TestAccountFunction(unittest.TestCase):

    def test_that_account_exist(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.assertTrue(self.account)

    def test_that_amount_can_be_deposited(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.account.deposit(5000)
        getBalance()
        self.assertEqual(self.account.getBalance(2), 5000)

    def test_that_amount_can_be_withdrawn(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.account.deposit(10000)
        self.account.withdraw(8000, 2)
        self.assertEqual(self.account.getBalance(2), 2000)

    def test_to_withdraw_twice(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.account.deposit(20000)
        getBalance()
        self.account.withdraw(10000, 2)
        getBalance()
        self.account.withdraw(5000, 2)
        self.assertEqual(self.account.getBalance(2), 5000)

    def test_to_withdraw_less_than_balance(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.account.deposit(1000)

        self.assertRaises(InsufficientAmountException, self.account.withdraw, -2000, 2)
        self.assertEqual(self.account.getBalance(2), 1000)

    def test_that_cannot_withdraw_more_than_balance(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.account.deposit(5000)
        self.assertEqual(self.account.getBalance(2), 5000)

        self.assertRaises(InsufficientAmountException, self.account.withdraw, 15000, 2)
        self.assertEqual(self.account.getBalance(2), 5000)

    def test_can_check_balance(self):
        self.account = Account("Ashley", "Ndabai", 2)
        self.assertEqual(self.account.getBalance(2), 0)

