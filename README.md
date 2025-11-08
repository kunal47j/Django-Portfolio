# Flask port of your Portfolio

This folder contains a minimal Flask wrapper that serves your existing frontend templates located in `main/templates` and static assets from `main/static`.

Quick start (Windows PowerShell):

1. Create and activate a virtual env (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements:

```powershell
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill your email credentials (or set environment variables):

```powershell
Copy-Item .env.example .env
# then edit .env with your editor
```

4. Run the app:

```powershell
python run.py
```

The app will run on http://127.0.0.1:5000 and will serve the same templates in `main/templates` and static files in `main/static`.

Routes added:
- `/` - homepage (renders `index.html`)
- `/contact` - POST endpoint for contact form (sends email using env vars)
- `/resume` - downloads the resume file from `static/media` if available

Security note: store passwords in environment variables or use a secret manager. Do not commit `.env` to git.
