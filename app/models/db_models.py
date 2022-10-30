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
    story_user_id: int # ID of the person that posted the story
    likes: int
    title: str
    theme: str
    startlat: float  # used to show starting point on map
    startlng: float
    # themes: List[str]  # 5 themes per story  #TODO: Make function that gets all themes for a story_id
    endlat: Optional[float] = None  # used to show starting point on map
    endlng: Optional[float] = None
    description: Optional[str] = None
    distance: Optional[float] = None
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
