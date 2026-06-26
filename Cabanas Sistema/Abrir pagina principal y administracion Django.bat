@echo off
set "PROJECT_DIR=C:\Users\carol\OneDrive\Desktop\proyecto_gestion_cabanas"
set "PYTHON_EXE=C:\Users\carol\OneDrive\Desktop\proyecto_gestion_cabanas\.venv\Scripts\python.exe"
set "PAGINA=http://127.0.0.1:8000/"
set "GESTION=http://127.0.0.1:8000/gestion/"

rem Liberar puerto 8000 si está ocupado
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do (
    taskkill /PID %%a /F
)

rem Arrancar Django en segundo plano
start "" /min "%PYTHON_EXE%" manage.py runserver 127.0.0.1:8000

rem Esperar unos segundos para que levante
timeout /t 3 >nul

rem Abrir páginas en el navegador
start "" "%PAGINA%"
start "" "%GESTION%"
