@echo off
title Iniciando Servidor Django - Alquileres Cabanas
cls

echo ===================================================
echo   INICIANDO SISTEMA DE GESTION DE CABANAS (Python 3.14)
echo ===================================================
echo.

:: 1. Ir a la raiz del proyecto
cd /d "C:\Users\carol\OneDrive\Desktop\alquileres_cabanas"

:: 2. Activar el entorno virtual de forma segura
echo [1/3] Activando entorno virtual (venv)...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo ERROR: NO SE ENCONTRÓ EL ENTORNO VIRTUAL EN venv\Scripts\activate.bat
    pause
    exit
)

:: 3. Abrir el navegador en la URL correcta (localhost) antes de bloquear la consola con el server
echo [2/3] Abriendo el navegador web...
start "" "http://localhost:8000/"

:: 4. Arrancar el servidor directamente desde la raíz (donde está tu manage.py real)
echo [3/3] Iniciando el servidor de desarrollo de Django...
echo.
python manage.py runserver

pause
