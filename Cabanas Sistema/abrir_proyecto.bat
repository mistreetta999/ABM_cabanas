
@echo off
REM Ir a la carpeta raíz del proyecto
cd /d "C:\Users\carol\OneDrive\Desktop\cabanas"

REM Activar entorno virtual (ajustá si tu venv tiene otro nombre)
call .venv\Scripts\activate

REM Levantar servidor Django (esto engloba todo el proyecto y todas las apps)
python manage.py runserver

pause
