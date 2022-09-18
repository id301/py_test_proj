import requests

from configuration import SERVICE2_URL
from baseclasses.response2 import Response
from src.pydantic_schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE2_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)