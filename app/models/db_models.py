"""
Defines the Pyantic models for the database.

These models are used to validate the data that is sent to the API.

"""

from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    """ Defines the model for a user. """
    user_id: int
    userUID: int
    username: str

    class Config:
        orm_mode = True


class Story(BaseModel):
    """ Defines the model for a story. """
    story_id: int
    user_id: int
    title: str
    ranking: int
    theme: str

    class Config:
        orm_mode = True


class Path(BaseModel):
    """ Defines the model for a path. """
    path_id: int
    story_id: int
    latitude: float
    longitude: float
    timestamp: int

    class Config:
        orm_mode = True


class Voice(BaseModel):
    """ Defines the model for a voice. """
    voice_id: int
    story_id: int
    order: int
    text: str
    start: int
    end: int

    class Config:
        orm_mode = True




