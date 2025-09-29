# api.py
import os
from fastapi import FastAPI
from services import FollowerService

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running!"}

@app.get("/analyze/followers")
def analyze_followers():
    follower_file = os.path.join("data", "connections", "followers_and_following", "followers_1.json")
    following_file = os.path.join("data", "connections", "followers_and_following", "following.json")

    service = FollowerService(follower_file, following_file)
    non_followers = service.unfollow_calculator()

    return {"non_followers": non_followers}
