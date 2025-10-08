import json
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import your service
from services import FollowerService


app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_and_analyze(
    followers: UploadFile = File(...),
    following: UploadFile = File(...)
):
    # Validate file types
    if followers.content_type != "application/json" or following.content_type != "application/json":
        return {"error": "Both files must be JSON"}

    try:
        followers_data = json.loads(await followers.read())
        following_data = json.loads(await following.read())
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in one of the files"}

    # Use your existing FollowerService with raw JSON instead of file paths
    service = FollowerService(followers_data, following_data)
    non_followers = service.unfollow_calculator()

    return {
        "message": "Analysis complete",
        "non_followers": non_followers
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)