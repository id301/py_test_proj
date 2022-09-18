import pytest
import requests

from configuration import SERVICE2_URL


@pytest.fixture(scope="session", autouse=True)
def say_hello():
    print("hello")
    return 14

@pytest.fixture(scope="function")
def get_users():
    response = requests.get(SERVICE2_URL)
    return response