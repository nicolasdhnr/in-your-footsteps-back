"""
Defines the Pyantic models for the database.

These models are used to validate the data that is sent to the API.

"""

from typing import Optional
from pydantic import BaseModel
from typing import Optional, Union, List


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
    ranking: int
    title: str
    theme: str
    path_id: int
    startlat: float  # used to show starting point on map
    startlng: float
    themes: List[str] # populated using the themes table


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
