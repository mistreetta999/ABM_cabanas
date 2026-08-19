$ErrorActionPreference = "Stop"

$ProjectDir = "C:\Users\carol\OneDrive\Desktop\cabanas"
$PythonExe = Join-Path $ProjectDir ".venv\Scripts\python.exe"
$ManagePy = Join-Path $ProjectDir "manage.py"
$Url = "http://127.0.0.1:8000/pagina_principal.html"
$OutLog = Join-Path $ProjectDir "django-launcher.out.log"
$ErrLog = Join-Path $ProjectDir "django-launcher.err.log"

Set-Location $ProjectDir

$serverRunning = $false
try {
    $connection = Test-NetConnection -ComputerName 127.0.0.1 -Port 8000 -WarningAction SilentlyContinue
    $serverRunning = [bool]$connection.TcpTestSucceeded
} catch {
    $serverRunning = $false
}

if (-not $serverRunning) {
    Start-Process -FilePath $PythonExe `
        -ArgumentList @($ManagePy, "runserver", "127.0.0.1:8000") `
        -WorkingDirectory $ProjectDir `
        -WindowStyle Hidden `
        -RedirectStandardOutput $OutLog `
        -RedirectStandardError $ErrLog

    Start-Sleep -Seconds 4
}

Start-Process $Url
