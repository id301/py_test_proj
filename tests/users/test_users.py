import requests
import pytest

from baseclasses.response2 import Response
from src.pydantic_schemas.user import User


def test_getting_users_list(get_users, make_number):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)
    #print(make_number)

@pytest.mark.production
@pytest.mark.skip
def test_another():
    assert 1 == 1

#Not optimal uniform tests
def test_calculation_positives(calculate):
    print(calculate(1, 2))

def test_calculation_one_negative(calculate):
    print(calculate(-2, 3))

def test_calculation_char(calculate):
    print(calculate("a", 1))

#optimal uniform tests
@pytest.mark.development
@pytest.mark.parametrize("first_value, second_value, result", [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ("b", -2, None),
    ("a", "b", None)
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
