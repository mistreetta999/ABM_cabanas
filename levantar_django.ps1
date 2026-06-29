# Ruta segura fuera de OneDrive
$SafePath = "C:\Projects\cabanas"

# Si la carpeta no existe, la crea
if (!(Test-Path $SafePath)) {
    New-Item -ItemType Directory -Path $SafePath | Out-Null
}

# Copia tu proyecto desde OneDrive a la carpeta segura
Copy-Item -Path "C:\Users\carol\OneDrive\Desktop\cabanas\*" -Destination $SafePath -Recurse -Force

# Cambia a la carpeta segura
Set-Location $SafePath

# Activa el entorno virtual
& ".\.venv\Scripts\Activate.ps1"

# Limpia caché de Python
Get-ChildItem -Path . -Include "__pycache__", "*.pyc" -Recurse -Force | Remove-Item -Recurse -Force

# Aplica migraciones
python manage.py makemigrations
python manage.py migrate

# Levanta el servidor Django en puerto 8000
Start-Process "http://127.0.0.1:8000/Gestion_Cabanas/"
python manage.py runserver 127.0.0.1:8000
