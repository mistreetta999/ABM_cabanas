import os
import subprocess
import webbrowser


def run_django():
    # Levanta el servidor Django
    subprocess.Popen(
        [
            "python",
            "manage.py",
            "runserver_plus",
            "--cert-file",
            "cert.pem",
            "--key-file",
            "key.pem",
        ]
    )
    # Abre el navegador en HTTPS
    webbrowser.open("https://127.0.0.1:8000")


if __name__ == "__main__":
    run_django()
