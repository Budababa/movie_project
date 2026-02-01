# main.py - Windows-kompatibilis indító script
import subprocess
import os
import sys

# BACKEND_URL beállítása
os.environ["BACKEND_URL"] = "https://movie-project-58bs.onrender.com"

# Backend indítása
backend_command = [sys.executable, "-m", "uvicorn", "backend.main:app", "--reload"]

# Frontend indítása
frontend_command = [sys.executable, "-m", "streamlit", "run", "frontend/app.py"]

# Backend futtatása külön processben
backend_process = subprocess.Popen(backend_command)

try:
    # Frontend futtatása
    subprocess.run(frontend_command)
finally:
    # Backend process leállítása a frontend bezárásakor
    backend_process.terminate()
