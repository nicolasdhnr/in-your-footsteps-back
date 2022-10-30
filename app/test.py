"""
Test heroku api endpoints.

"""

import requests
import json
import pytest
from app.models.data_transfer_models import UserIn, StoryIn, PathIn, VoiceIn

heroku_url = "https://in-your-footsteps.herokuapp.com/"


def test_signin():
    url = heroku_url + "login/"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {'login': 'success'}
    print(response.json())

def test_signup():
    user = UserIn(userUID=123456789, username="test")
    response = requests.post(heroku_url + "signup/", json=user.dict())
    assert response.status_code == 200
    assert response.json() == user.dict()
    print(response.json())


