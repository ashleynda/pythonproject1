import unittest

from tests.accountexceptions import InsufficientAmountException
from tests.bank import Bank
from tests.bankexceptions import NonExistentAccount, AmountNotEnoughException


class TestBankFunction(unittest.TestCase):

    def test_that_we_can_register_customers(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())

    def test_that_we_can_find_account(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.bank.find_account("1")
        self.assertRaises(NonExistentAccount, self.bank.find_account("1"))

    def test_that_we_can_deposit(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
        self.bank.deposit(5000, "1")
        self.assertEqual(5000, self.bank.checkBalance("1", '1234'))

    def test_that_amount_can_be_withdrawn(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
        self.bank.deposit(10000, "1")
        self.bank.withdraw("1", 5000, "1234")
        self.assertEqual(5000, self.bank.checkBalance("1", "1234"))

    def test_that_amount_can_be_withdrawn_twice(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
        self.bank.deposit(10000, "1")
        self.bank.withdraw("1", 5000, "1234")
        self.assertEqual(5000, self.bank.checkBalance("1", "1234"))
        self.bank.withdraw("1", 2000, "1234")
        self.assertEqual(3000, self.bank.checkBalance("1", "1234"))

    def test_that_cannot_withdraw_less_than_balance(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
        self.bank.deposit(10000, "1")
        self.assertRaises(InsufficientAmountException, self.bank.withdraw, "1", -5000, "1234")

    def test_that_cannot_withdraw_more_than_amount(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
        self.bank.deposit(10000, "1")
        self.assertRaises(InsufficientAmountException, self.bank.withdraw, "1", 30000, "1234")

    def test_that_can_checkBalance(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
        self.assertEqual(0, self.bank.checkBalance("1", '1234'))
        self.bank.deposit(5000, "1")
        self.assertEqual(5000, self.bank.checkBalance("1", '1234'))

    def test_that_can_transfer_from_account_to_account(self):
        self.bank = Bank()
        self.bank.register("Ashley", "Ndabai", "1234")
        self.assertEqual("Ashley Ndabai", self.bank.find_account("1").get_account_name())
