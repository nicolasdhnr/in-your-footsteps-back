"""
Defines all relevant API endpoints.
"""
from fastapi import FastAPI
import asyncio
from app.models.db_models import User, Story, Path, Voice
from app.models.data_transfer_models import UserIn, StoryIn, PathIn, VoiceIn, HandshakeIn, HandshakeOut
from app.db.manipulation import data_to_db
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/handshake/")
def handshake(handshake: HandshakeIn):
    print(handshake)
    return handshake



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

#testing firestore connection
@app.get("/firestore/")
def get_path_data():
    pass
