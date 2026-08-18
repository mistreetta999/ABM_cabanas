import os
import subprocess
import webbrowser
import time

# Activar entorno virtual (opcional si ya está activo)
venv_path = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")

# Levantar servidor Django
server = subprocess.Popen([venv_path, "manage.py", "runserver"])

# Esperar unos segundos para que arranque
time.sleep(3)

# Abrir navegador en la app
webbrowser.open("http://127.0.0.1:8000/")

# Mantener el servidor corriendo
server.wait()
