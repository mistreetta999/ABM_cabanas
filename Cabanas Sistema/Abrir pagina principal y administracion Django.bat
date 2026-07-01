@echo off
setlocal

rem Usa la carpeta donde está este .bat (Cabanas Sistema)
set "SCRIPT_DIR=%~dp0"

rem Proyecto real: carpeta padre del .bat
for %%I in ("%SCRIPT_DIR%..") do set "PROJECT_DIR=%%~fI"

set "PYTHON_EXE=%PROJECT_DIR%\.venv\Scripts\python.exe"
set "URL_PAGINA=http://127.0.0.1:8000/pagina_principal/"
set "DJANGO_GESTION_CABANAS_URL=http://127.0.0.1:8000/gestion_cabanas/"
if not exist "%PYTHON_EXE%" (
    echo [ERROR] No se encontro Python del entorno virtual:
    echo %PYTHON_EXE%
    pause
    exit /b 1
)

if not exist "%PROJECT_DIR%\manage.py" (
    echo [ERROR] No se encontro manage.py en:
    echo %PROJECT_DIR%
    pause
    exit /b 1
)

rem Liberar puerto 8000 si esta ocupado
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do (
    taskkill /PID %%a /F >nul 2>&1
)

rem Arrancar Django minimizado
start "Django Cabanas" /min cmd /c "cd /d %PROJECT_DIR% && %PYTHON_EXE% manage.py runserver 127.0.0.1:8000"

rem Esperar arranque
timeout /t 3 /nobreak >nul

rem Abrir paginas
start "" "%URL_PAGINA%"
start "" "%DJANGO_GESTION_CABANAS_URL%"
endlocal
