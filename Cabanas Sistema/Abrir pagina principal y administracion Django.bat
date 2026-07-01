@echo off
REM Activar entorno virtual
cd /d "C:\Users\carol\OneDrive\Desktop\cabanas"
call .venv\Scripts\activate

REM Abrir servidor Django
start "" python manage.py runserver

REM Abrir navegador en página principal
start "" http://127.0.0.1:8000/interfaz/

REM Abrir navegador en administración Django
start "" http://127.0.0.1:8000/admin/

pause
