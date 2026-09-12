$carpetas = @("cabanas_project","cabanas_api","cabanas_principal","django_core","src","static","Templates")

foreach ($c in $carpetas) {
    if (Test-Path $c) {
        Write-Host "Carpeta activa:" $c
        Get-ChildItem $c
    }
}

# Ir a la carpeta con manage.py y levantar el servidor
Set-Location "django_core"
python manage.py runserver
