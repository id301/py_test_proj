import requests

from baseclasses.response2 import Response
from src.pydantic_schemas.user import User


def test_getting_users_list(get_users):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)