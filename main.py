"""
Defines all relevant API endpoints.
"""
from fastapi import FastAPI
import asyncio
from app.models.db_models import User, Story, Path, Voice
from app.models.data_transfer_models import UserIn, StoryIn, StoryIn, StoryStartIn, HandshakeIn, HandshakeOut, \
    StoryStartOut, Recording
from app.db.manipulation import data_to_db

from fastapi.middleware.cors import CORSMiddleware
import json

from typing import List, Union

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/handshake/")
async def handshake(handshake: HandshakeIn) -> dict:
    # get handshake data from db
    # return handshake data

    handshake_out = HandshakeOut(stories=[story_1, story_2, story_3, story_4, story_5])
    return handshake_out.dict()


# User wants to like a story.
@app.post("/like/")
async def like(story_id: int) -> dict:
    # increment story ranking in db based

    return {f"Story {story_id}": "liked"}


@app.post("/unlike/")
async def unlike(story_id: int) -> dict:
    # decrement story ranking in db based

    return {f"Story {story_id}": "unliked"}


# User finishes recording a story
@app.post("/log_path/")
async def log_story(story: StoryIn):
    """
    Register a new story.
    """
    # log path to db
    # write data to db

    return {f"path {story.storyID}": "logged"}


# User presses the confirm story button and starts following a path
@app.post("/confirm_story/")
async def confirm_story(story: StoryStartIn) -> dict:
    """
    Register a new story.
    :param path:
    :return:
    """
    # receive the story id
    # get every recordg associated with the story id in the database
    # return the recordings to the front end
    recording_1 = Recording(voice_id=1, start_lat=1.1, start_lng=1.1)
    recording_2 = Recording(voice_id=2, start_lat=2.2, start_lng=2.2)
    recording_3 = Recording(voice_id=3, start_lat=3.3, start_lng=3.3)
    recording_4 = Recording(voice_id=4, start_lat=4.4, start_lng=4.4)

    story_out = StoryStartOut(story_id=1, user_id=1, ranking=1, title="test", theme="test", startlat=1.1, startlng=1.1,
                              path_id=1)
    return story_out.dict()


@app.get("/seach/")
async def search(title: str) -> List[Story]:
    # search db by title
    # return list of stories

    return  # FILL


app.get("/filter/{theme}")
async def filter(theme: str) -> List[Story]:
    # search db by theme
    # return list of stories
    return  # FILL


# testing firestore connection
@app.get("/firestore/")
def get_path_data():
    pass
