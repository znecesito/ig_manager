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
- **Language**: Python  
- **Interface**: Command-line (frontend planned in future versions)  

---

## 📦 Installation & Setup
1. Clone the repository:
```bash
   git clone https://github.com/yourusername/ig-manager.git
   cd ig-manager
```
<!-- 2. Make sure you have Python 3.8+ installed.
Install dependencies (if you have a requirements.txt):
```bash
pip install -r requirements.txt
```-->


---

## ▶️ Usage
1. Export your Instagram data from Meta (profile → Settings → Privacy and Security → Download Data).
2. Place the exported data (JSON/ZIP) inside the project directory.
3. Run the script:
```bash
python main.py
```
4. Follow the command-line prompts.

---

## 📊 Current Status
- ✅ **Follower analysis** – working but CLI-only.
- ⚠️ **Message analysis** – functional but incomplete, requires manual guidance.
- 🔮 **Planned** – web/desktop frontend for easier usage.

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
