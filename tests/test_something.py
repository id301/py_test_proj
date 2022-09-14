## https://my-json-server.typicode.com/typicode/demo/posts
import requests

from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA
from baseclasses.response import Response


def test_getting_posts():
    response = Response(requests.get(url=SERVICE_URL))
    response.assert_status_code(200).validate(POST_SCHEMA)
    response.assert_count(3)