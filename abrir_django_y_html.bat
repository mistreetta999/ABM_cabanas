@echo off
setlocal

cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

start "Django Cabanas" /min "%PYTHON%" manage.py runserver 127.0.0.1:8000
timeout /t 3 /nobreak > true
start "" "http://127.0.0.1:8000/panel-django/"
start "" "%~dp0html_local\presentacion_cabanas.html"

endlocal
