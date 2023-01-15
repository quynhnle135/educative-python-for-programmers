import pytest

from object_oriented_programming.information_hiding.student import *

@pytest.fixture
def test_student():
    student = Student()
    student.setName("Quinn")
    student.setRollNumber(1234)
    return student


def test_get_name(test_student):
    assert test_student.getName() == "Quinn"


def test_get_roll_number(test_student):
    assert test_student.getRollNumber() == 1234

