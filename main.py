"""
Defines all relevant API endpoints.
"""
from fastapi import FastAPI
import asyncio
from app.models.db_models import User, Story, Path, Voice
from app.models.data_transfer_models import UserIn, StoryIn, PathIn, VoiceIn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# sign up
@app.post("/signup/")
def signup(user: UserIn):
    return user


@app.get("/login/")
def login():
    return {"login": "success"}
