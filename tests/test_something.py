## https://my-json-server.typicode.com/typicode/demo/posts
import requests
import json

from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from auxilaries import post

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    assert post.is_field_in_post(received_posts[0], "id"), GlobalErrorMessages.EXPECTED_FIELD_NOT_EXISTS.value + " - id"
    assert post.is_field_in_post(received_posts[0], "title"), GlobalErrorMessages.EXPECTED_FIELD_NOT_EXISTS.value + " - title"


#def is_field_in_post(post, field):
#    return field in post