@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

echo Aplicando migraciones...
"%PYTHON%" manage.py migrate
if errorlevel 1 (
    echo Error al aplicar migraciones.
    pause
    exit /b 1
)

echo Levantando servidor en http://127.0.0.1:8000/
"%PYTHON%" manage.py runserver 127.0.0.1:8000

endlocal
