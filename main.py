# main.py - Windows & venv kompatibilis indító script
import subprocess
import os
import sys

# --- BACKEND_URL beállítása ---
os.environ["BACKEND_URL"] = "https://movie-project-58bs.onrender.com"

# --- VENV Python meghatározása ---
# Ha a venv-et a script mellett hoztad létre
venv_python = os.path.join(os.path.dirname(__file__), "venv", "Scripts", "python.exe")

if not os.path.exists(venv_python):
    print("Hiba: Nem található a virtuális környezet Python-ja!")
    print("Kérlek ellenőrizd, hogy létre van-e hozva a venv mappa a projekt gyökerében.")
    sys.exit(1)

# --- Backend indítása ---
backend_command = [venv_python, "-m", "uvicorn", "backend.main:app", "--reload"]

# --- Frontend indítása ---
frontend_command = [venv_python, "-m", "streamlit", "run", "frontend/app.py"]

# --- Backend futtatása külön processben ---
backend_process = subprocess.Popen(backend_command)

try:
    # Frontend futtatása
    subprocess.run(frontend_command)
finally:
    # Backend leállítása a frontend bezárásakor
    backend_process.terminate()
