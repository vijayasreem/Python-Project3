# sb_acc.py

import random
import sb_etc as etc
from enum import Enum


# Bank Accounts
class AccountNullError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Client():
    def __init__(self, Name, Gender, Age):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age


class Account(Client):
    def __init__(self, Name, Gender, Age):
        super().__init__(Name, Gender, Age)
        self.Balance = 0
        self.AccountNumber = etc.fixedrandom(24)
        etc.Debug(f"Created Account({Name}, {Gender}): {self.AccountNumber}")

    @classmethod
    def Deposit(self, Amount):
        self.Balance += Amount

    @classmethod
    def Withdraw(self, Amount):
        self.Balance -= Amount


class Card(Account):
    def __init__(self, Account):
        self.CardNumber = etc.fixedrandom(20)
        self.Expiry = etc.getExpiry()
        self.PIN = etc.fixedrandom(4)
        etc.Debug(f"DEBUG: Created Card {self.CardNumber}:{self.Expiry}:{self.PIN}")
        etc.Debug(f"Associated account: {Account.AccountNumber}")
