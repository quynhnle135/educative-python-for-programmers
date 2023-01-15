import pytest

from object_oriented_programming.information_hiding.rectangle import *

@pytest.fixture
def test_rectangle():
    rec = Rectangle(4, 5)
    return rec


def test_find_area(test_rectangle):
    assert test_rectangle.find_area() == 20


def test_find_perimeter(test_rectangle):
    assert test_rectangle.find_perimeter() == 18