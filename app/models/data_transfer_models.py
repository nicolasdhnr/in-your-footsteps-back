from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserIn(BaseModel):
    """ Defines the model for a user. """
    userUID: int
    username: str


class StoryIn(BaseModel):
    """ Defines the model for a story. """
    user_id: int
    title: str
    ranking: int
    theme: str


class PathIn(BaseModel):
    """ Defines the model for a path. """
    story_id: int
    latitude: float
    longitude: float
    timestamp: int


# todo: Maybe we don't need to send the UID every time? - start flag then assumes same story uid unless otherwise specified.
class VoiceIn(BaseModel):
    """ Defines the model for a voice. """
    story_id: int
    order: int
    text: str
    start: int
    end: int
