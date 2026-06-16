@echo off
set "PROJECT_DIR=C:\Users\carol\OneDrive\Desktop\proyecto_gestion_cabanas"
set "PYTHON_EXE=C:\Users\carol\OneDrive\Desktop\proyecto_gestion_cabanas\.venv\Scripts\python.exe"
set "PAGINA=http://127.0.0.1:8000/"
set "GESTION=http://127.0.0.1:8000/gestion/"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$port=8000; $running=Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue; if (-not $running) { Start-Process -FilePath '%PYTHON_EXE%' -ArgumentList 'manage.py runserver 127.0.0.1:8000' -WorkingDirectory '%PROJECT_DIR%' -WindowStyle Minimized; Start-Sleep -Seconds 3 }; Start-Process '%PAGINA%'; Start-Process '%GESTION%'"
