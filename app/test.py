"""
Test heroku api endpoints.

"""

import requests
import json
import pytest
from app.models.data_transfer_models import UserIn, StoryIn, PathIn, VoiceIn

heroku_url = "https://footsteps-api.herokuapp.com/"


def test_signin():
    response = requests.get(heroku_url + "login/")
    assert response.status_code == 200
    assert response.json() == {"login": "success"}
    print(response.json())

def test_signup():
    user = UserIn(userUID=123456789, username="test")
    response = requests.post(heroku_url, json=user.dict())
    assert response.status_code == 200
    assert response.json() == user.dict()
    print(response.json())


