@echo off
REM Ir a la carpeta raíz del proyecto
cd /d "C:\Users\carol\OneDrive\Desktop\cabanas"

REM Activar entorno virtual (ajustá si tu venv tiene otro nombre)
call .venv\Scripts\activate

REM Levantar TODO el proyecto Django
python manage.py runserver

REM Abrir navegador en la página principal del sistema
start "" http://127.0.0.1:8000/
