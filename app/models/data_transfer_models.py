from pydantic import BaseModel
from typing import Optional, Union, List
from datetime import datetime
from app.models.db_models import User, Story, Path, Voice


class HandshakeIn(BaseModel):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    """ Defines the model for a user. """
    userUID: int
    username: str


class StoryOut(BaseModel):
    """ Defines the model for a story. """
    story_id: int
    user_id: int # user who posted it
    start_latitude: float  # used to show starting point on map
    start_longitude: float


class StoryRecomendation(BaseModel):
    """ Defines the model for the story recommendations. """
    story_list: Union[List[Story], None]  # Pass the top 50 recommendations


class StoryIn(BaseModel):
    """ New Story registration. """
    story_id: str
    startlat: float
    startlng: float
    story_user_id: int # id of the user who just created the ting
    title : str
    description : str


# todo: Maybe we don't need to send the UID every time? - start flag then assumes same story uid unless otherwise specified.
# Hanshake Stuff
class HandshakeOut(BaseModel):
    """ Defines the model for the initial exchange of information. """
    # NOTE: Handshake should be called every time the UI is refreshed."
    stories: List[Union[Story, None]]

    class Config:
        orm_mode = True


# ============  Sending and receiving audio ============
class StoryStartIn(BaseModel):
    """ Story Start. """
    story_id: int


class Recording(BaseModel):
    """ Defines the model for a recording. """
    recording_id: int
    startlat: int
    endlat: Optional[int] = None


class StoryStartOut(BaseModel):
    """ Defines the model for a request for an audio file. """
    recordings: List[Recording]
