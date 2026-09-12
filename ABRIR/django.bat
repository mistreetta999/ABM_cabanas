@echo off
setlocal
set "PROYECTO=%~dp0"
set "INICIADOR=%PROYECTO%abrir_sistema.vbs"
set "NOMBRE_ACCESO=Cabanas Espindola.lnk"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$desktop=[Environment]::GetFolderPath('Desktop');" ^
    "$shell=New-Object -ComObject WScript.Shell;" ^
    "$shortcut=$shell.CreateShortcut((Join-Path $desktop '%NOMBRE_ACCESO%'));" ^
    "$shortcut.TargetPath='wscript.exe';" ^
    "$shortcut.Arguments='\"%INICIADOR%\"';" ^
    "$shortcut.WorkingDirectory='%PROYECTO%';" ^
    "$shortcut.IconLocation='%SystemRoot%\System32\shell32.dll,220';" ^
    "$shortcut.Save();"

echo.
echo Acceso directo reparado en el escritorio: %NOMBRE_ACCESO%
echo.
pause
