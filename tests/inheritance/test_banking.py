import pytest

from object_oriented_programming.inheritance.banking import *

@pytest.fixture
def test_account():
    account = Account("Mark", 5000)
    return account

@pytest.fixture
def test_saving_account():
    saving_account = SavingsAccount("Mark", 5000, 5)
    return saving_account


def test_withdrawal(test_account):
    test_account.withdrawal(1000)
    assert test_account.getBalance() == 4000


def test_deposit(test_account):
    test_account.deposit(1000)
    assert test_account.getBalance() == 6000


def test_interest_amount(test_saving_account):
    expected = (5000 * 5) / 100
    assert test_saving_account.interestAmount() == expected


def test_account_str(test_account):
    assert test_account.__str__() == f"Title is Mark and Balance is 5000"

