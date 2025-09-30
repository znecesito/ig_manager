# main.py
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse
import json
import uvicorn

app = FastAPI()

# HTML form for file upload
html_form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Upload JSON</title>
    </head>
    <body>
        <h1>Upload a JSON file</h1>
        <form action="/upload" enctype="multipart/form-data" method="post">
            <input name="file" type="file" accept=".json">
            <input type="submit" value="Upload">
        </form>
    </body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_form

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "application/json":
        return {"error": "File is not JSON"}

    # Read file contents
    contents = await file.read()
    try:
        data = json.loads(contents)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}

    # Print JSON to console for validation
    print("Uploaded JSON content:")
    print(json.dumps(data, indent=4))

    return {"message": "JSON uploaded and printed to console successfully", "data": data}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
