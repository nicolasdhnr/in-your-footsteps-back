from pydantic import BaseModel
from typing import Optional, Union, List
from datetime import datetime


class HandshakeIn(BaseModel):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class HandshakeOut(BaseModel):
    """ Defines the model for the initial exchange of information. """
    # NOTE: Handshake should be called every time the UI is refreshed."

    user_id: int
    stories: list

    class Config:
        orm_mode = True


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


class StoryOut(BaseModel):
    """ Defines the model for a story. """
    story_id: int
    user_id: int
    start_latitude: float  # used to show starting point on map
    start_longitude: float


class StoryRecomendation(BaseModel):
    """ Defines the model for the story recommendations. """
    story_list: Union[List[StoryOut], None]  # Pass the top 50 recommendations


class PathIn(BaseModel):
    """ Defines the model for a path. """
    path: List[dict]  # list of dicts with lat, long, timestamp


# todo: Maybe we don't need to send the UID every time? - start flag then assumes same story uid unless otherwise specified.
class VoiceIn(BaseModel):
    """ Defines the model for a voice. """
    story_id: int
    order: int
    text: str
    start: int
    end: int


# Sending and receiving qudio
class AudioFileRequestIN(BaseModel):
    """ Defines the model for a request for an audio file. """
    story_id: int
    timestamp: int


class AudioFileRequestOUT(BaseModel):
    """ Defines the model for a request for an audio file. """
    story_id: int
    timestamp: int
    audio_file_link: str
