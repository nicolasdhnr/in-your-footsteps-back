"""
Defines all relevant API endpoints.
"""
from fastapi import FastAPI
import asyncio
from app.models.db_models import User, Story, Path, Voice
from app.models.data_transfer_models import UserIn, StoryIn, StoryIn, StoryStartIn, HandshakeIn, HandshakeOut, \
    StoryStartOut, Recording
from app.db.manipulation import insert_new_story, get_nearest, search_by_title, search_by_theme, upvote, downvote, recordings_per_story
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
    handshake_out = get_nearest(handshake.latitude, handshake.longitude)
    return handshake_out.dict()


# User wants to like a story.
@app.post("/like/")
async def like(story_id: int) -> dict:
    # increment story ranking in db based
    upvote(story_id)
    return {f"Story {story_id}": "liked"}


@app.post("/unlike/")
async def unlike(story_id: int) -> dict:
    # decrement story ranking in db based
    downvote(story_id)
    return {f"Story {story_id}": "unliked"}


# User finishes recording a story
@app.post("/log_path/")
async def log_story(story: StoryIn):
    """
    Register a new story.
    """
    # log path to db
    # write data to db
    insert_new_story(story)
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

    return recordings_per_story(story.story_id)

@app.get("/seach/")
async def search(title: str) -> List[Story]:
    # search db by title
    # return list of stories

    return search_by_title(title).json()


@app.get("/filter/{theme}")
async def filter(theme: str) -> List[Story]:
    # search db by theme
    # return list of stories
    return search_by_theme(theme).json()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


