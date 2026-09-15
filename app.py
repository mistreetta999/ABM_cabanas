"""Launcher para Django con uvicorn (ASGI)"""

import os
import webbrowser
import uvicorn

def main():
    # Configuración mínima de Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.cabana_proyect.settings")

    # Abrir navegador automáticamente en HTTPS
    webbrowser.open("https://localhost:8000")

    # Ejecutar uvicorn con certificados SSL
    uvicorn.run(
        "django_core.core.asgi:application",
        host="0.0.0.0",
        port=8000,
        ssl_certfile="cert.pem",
        ssl_keyfile="key.pem"
    )

if __name__ == "__main__":
    main()
