# IG Manager

A command-line tool for analyzing your Instagram data.  

Currently, IG Manager supports two main use cases:

1. **Follower Analysis** – Check who you follow that do not follow you back.  
2. **Message Analysis** – Explore patterns in your Instagram messages (experimental / work-in-progress).  

---

## 🚀 Features
- Parse exported Instagram data from Meta.  
- Return accurate lists of accounts that don’t follow back.  
- Early-stage message analysis (requires manual steps to run).  

---

## 🛠️ Tech Stack
- **Backend (Python)**: Python  
  - Framework: FastAPI
  - Server: Uvicorn
  - Data Handling: JSON, Custom Service Classes
- **Frontend**: JavaScript/React  
  - Framework: React (create-react-app style structure)
  - Styling: Inline CSS styles


---

## 📦 Installation & Setup
This project requires both Python and Node.js/npm to run locally.
1. Clone the repository:
```bash
   git clone https://github.com/yourusername/ig-manager.git
   cd ig-manager
```
2. Make sure you have Python 3.8+ installed.

    **Optional**: Create and activate a Python virtual environment
    ```bash
    python3 -m venv venv
    ```
    Linux/macOS: source venv/bin/activate
    
    Windows: .\venv\Scripts\activate
3. Set up the backend:
```bash
pip install -r requirements.txt
```
4. Set up the frontend:
```bash
cd frontend
npm install
```

---

## ▶️ Usage
You need two terminal windows open to run the full application:
1. Run the Backend API (Port 8000)
    
    In your main project directory terminal:
    ```bash
    python main.py
    ```
    The API will be live at http://127.0.0.1:8000.
2. Run the Frontend UI (Port 3000)
   
    In your frontend directory terminal: 
    ```bash
    cd frontend
    npm start
    ```
   The application will open in your browser at http://localhost:3000.
3. Use the app
   - **Export Data**: Export your Instagram data from Meta in **JSON** format (profile → Settings → Privacy and Security → Download Data).
   - **Upload**: Use the UI at http://localhost:3000 to upload your followers.json and following.json files.
   - **Analyze**: The app will display a list of users you follow who haven't followed you back.


---

## 📊 Current Status
- ✅ **Follower analysis** – working UI.
- ⚠️ **Message analysis** – in progress.
- 🔮 **Planned** – production deployment via K8s.

---

## 🤝 Contributing
This project is early-stage, but contributions are welcome!
Fork the repo and create a feature branch (git checkout -b feature-xyz).
Submit a pull request.
Direct pushes to main are not allowed.

---

## 📜 License

Currently unlicensed. 

⚡ Note: IG Manager is not affiliated with Meta/Instagram. You must only analyze data you’ve exported from your own account.
