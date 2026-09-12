$carpetas = @("cabanas_project","cabanas_api","cabanas_principal","django_core","src","static","Templates","public","web","staticfile","static","DATABASE","AppConfig")

foreach ($c in $carpetas) {
    if (Test-Path $c) {
        Write-Host "Carpeta activa:" $c
        Get-ChildItem $c
    }
}
