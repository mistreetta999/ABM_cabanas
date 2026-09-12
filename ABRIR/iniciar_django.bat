@echo off
cd /d "C:\Users\carol\OneDrive\Desktop\cabanas"
call .venv312\Scripts\activate
python manage.py runserver
pause
@echo off
start "" http://127.0.0.1:8000/
@echo off
REM Activa el entorno virtual y levanta Django, luego abre la página principal

cd /d "C:\Users\carol\OneDrive\Desktop\cabanas"
call .venv312\Scripts\activate
start "" python manage.py runserver
timeout /t 5 >nul
start "" http://127.0.0.1:8000/alquileres_cabanas.dj/
@echo off
REM Ir a la carpeta raíz del proyecto
cd /d "C:\Users\carol\OneDrive\Desktop\cabanas"

REM Activar entorno virtual (ajusta si tu venv tiene otro nombre)
call .venv\Scripts\activate

REM Levantar servidor Django en segundo plano
start "" python manage.py runserver

REM Abrir navegador en la página principal
start "" http://127.0.0.1:8000/pagina_principal.html/

REM Abrir admin en segundo plano (no interfiere con la página principal)
start "" http://127.0.0.1:8000/admin/

REM Abrir admin en segundo plano (no interfiere con la página principal)
start "" http://127.0.0.1:8000/alquileres_cabanas.dj/admin/

pause
