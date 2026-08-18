from __future__ import annotations

import subprocess
import time
import webbrowser
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
PYTHON = PROJECT_DIR / ".venv" / "Scripts" / "python.exe"
MANAGE = PROJECT_DIR / "manage.py"
PUBLIC_DIR = PROJECT_DIR / "public"


def ejecutar_check_django() -> bool:
    print("Verificando Django...")
    resultado = subprocess.run(
        [str(PYTHON), str(MANAGE), "check"],
        cwd=PROJECT_DIR,
        text=True,
    )
    return resultado.returncode == 0


def iniciar_django() -> subprocess.Popen[str] | None:
    print("Levantando Django con la configuracion por defecto de runserver...")
    return subprocess.Popen(
        [
            str(PYTHON),
            str(MANAGE),
            "runserver",
            "--noreload",
        ],
        cwd=PROJECT_DIR,
        text=True,
    )


def validar_archivos() -> None:
    faltantes = [
        ruta
        for ruta in (
            PYTHON,
            MANAGE,
            PUBLIC_DIR / "index.html",
            PUBLIC_DIR / "pagina_principal.html",
        )
        if not ruta.exists()
    ]

    if faltantes:
        nombres = "\n".join(str(ruta) for ruta in faltantes)
        raise FileNotFoundError(f"Faltan archivos necesarios:\n{nombres}")


def abrir_paginas() -> None:
    paginas = [
        PUBLIC_DIR / "pagina_principal.html",
        PUBLIC_DIR / "index.html",
    ]

    print("Abriendo paginas HTML locales...")
    for pagina in paginas:
        webbrowser.open(pagina.resolve().as_uri())


def detener_procesos(procesos: list[subprocess.Popen[str]]) -> None:
    for proceso in procesos:
        if proceso.poll() is None:
            proceso.terminate()


def main() -> int:
    procesos: list[subprocess.Popen[str]] = []

    try:
        validar_archivos()

        if not ejecutar_check_django():
            print("Django tiene errores. Revisar la salida anterior.")
            return 1

        django = iniciar_django()
        if django is not None:
            procesos.append(django)

        time.sleep(3)
        print()
        print("Django quedo iniciado con runserver.")
        print("Las paginas HTML publicas se abren como archivos locales.")
        print()

        abrir_paginas()

        print("Deja esta ventana abierta para mantener vivos los servidores iniciados.")
        print("Para cerrar, presiona Ctrl+C.")

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCerrando servidores iniciados por este mediador...")
        detener_procesos(procesos)
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        detener_procesos(procesos)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
