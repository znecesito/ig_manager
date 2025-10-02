import json
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import uvicorn

# Import your service
from services import FollowerService

app = FastAPI()

# HTML form for file upload
html_form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Upload JSON</title>
    </head>
    <body>
        <h1>Upload Followers/Following JSON files</h1>
        <form action="/upload" enctype="multipart/form-data" method="post">
            <label>Followers JSON:</label>
            <input name="followers" type="file" accept=".json"><br><br>
            <label>Following JSON:</label>
            <input name="following" type="file" accept=".json"><br><br>
            <input type="submit" value="Upload & Analyze">
        </form>
    </body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_form


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