import pytest

from object_oriented_programming.calculator import *

@pytest.fixture
def my_calculator():
    return Calculator(2, 3)


def test_add(my_calculator):
    assert my_calculator.add() == 5


def test_subtract(my_calculator):
    assert my_calculator.subtract() == 1


def test_multiply(my_calculator):
    assert my_calculator.multiply() == 6


def test_divide(my_calculator):
    expected = 3 // 2
    assert my_calculator.divide() == expected
