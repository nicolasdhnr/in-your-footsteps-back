"""
Defines all relevant API endpoints.
"""
from fastapi import FastAPI
import asyncio
from app.models.db_models import User, Story, Path, Voice
from app.models.data_transfer_models import UserIn, StoryIn, PathIn, VoiceIn, HandshakeIn, HandshakeOut
from app.db.manipulation import data_to_db
from fastapi.middleware.cors import CORSMiddleware
import json
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
async def handshake(handshake: HandshakeIn) -> HandshakeOut:
    story_1 = StoryIn(user_id=1, title="test", ranking=1, theme="test")
    story_2 = StoryIn(user_id=2, title="test", ranking=2, theme="test")
    story_3 = StoryIn(user_id=3, title="test", ranking=3, theme="test")
    story_4 = StoryIn(user_id=4, title="test", ranking=4, theme="test")
    story_5 = StoryIn(user_id=5, title="test", ranking=5, theme="test")
    handshake_out = HandshakeOut(stories=[story_1, story_2, story_3, story_4, story_5])
    return handshake_out.dict()


# sign up
@app.post("/signup/")
def signup(user: UserIn):
    return user


@app.get("/login/")
def login():
    return {"login": "success"}


@app.post("/story/")
def create_story(story: StoryIn):
    return story


@app.post("/path/")
def create_path(path: PathIn):
    return path


# testing firestore connection
@app.get("/firestore/")
def get_path_data():
    pass
