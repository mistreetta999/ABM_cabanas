""" para verificar la estructura de un proyecto Django """
import os
from typing import Any
# Carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Archivos y carpetas obligatorios
estructura = [
    "cabanas/__init__.py",
    "cabanas/settings.py",
    "cabanas/urls.py",
    "cabanas/wsgi.py",
    "cabanas/asgi.py",
    "manage.py",
    "cabanas_api/__init__.py",
    "cabanas_api/apps.py",
    "cabanas_api/models.py",
    "cabanas_api/views.py",
    "cabanas_api/admin.py",
    "cabanas_api/tests.py",
    "cabanas_api/migrations/__init__.py",
]

def verificar()->None:
    print("🔍 Verificando estructura del proyecto Django...\n")
    faltantes = []
    for item in estructura:
        ruta = os.path.join(BASE_DIR, item)
        if os.path.exists(ruta):
            print(f"✅ Existe: {item}")
        else:
            print(f"❌ Falta: {item}")
            faltantes.append(item)

    if not faltantes:
        print("\n🎉 Todo está en orden, tu proyecto tiene la estructura completa.")
    else:
        print("\n⚠️ Archivos/carpetas faltantes:")
        for f in faltantes:
            print(f"   - {f}")

if __name__ == "__main__":
    verificar()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

estructura:list = [
    "cabanas/__init__.py",
    "cabanas/settings.py",
    "cabanas/urls.py",
    "cabanas/wsgi.py",
    "cabanas/asgi.py",
    "manage.py",
    "cabanas_api/__init__.py",
    "cabanas_api/apps.py",
    "cabanas_api/models.py",
    "cabanas_api/views.py",
    "cabanas_api/admin.py",
    "cabanas_api/tests.py",
    "cabanas_api/migrations/__init__.py",
]

def verificar()->None:
    print("🔍 Verificando estructura del proyecto Django...\n")
    faltantes = []
    for item in estructura:
        ruta = os.path.join(BASE_DIR, item)
        if os.path.exists(ruta):
            print(f"✅ Existe: {item}")
        else:
            print(f"❌ Falta: {item}")
            faltantes.append(item)

    if not faltantes:
        print("\n🎉 Todo está en orden, tu proyecto tiene la estructura completa.")
    else:
        print("\n⚠️ Archivos/carpetas faltantes:")
        for f in faltantes:
            print(f"   - {f}")

if __name__ == "__main__":
    verificar()
import os

# Carpeta raíz del proyecto (ajusta si no coincide)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Lista de carpetas críticas que deben existir
carpetas = [
    "cabanas_project",
    "cabana_apps",
    "cabana_apps/migrations",
    "chatbot",
    "chatbot/migrations",
    "templates",
    "templates/cabanas",
    "templates/reservas",
    "templates/chatbot",
    "static",
    "static/css",
    "static/js",
    "static/img",
    "media"   # para archivos subidos por usuarios
]

def verificar_carpetas():
    print("🔍 Verificando estructura de carpetas...\n")
    for carpeta in carpetas:
        ruta = os.path.join(BASE_DIR, carpeta)
        if os.path.exists(ruta):
            print(f"✅ Existe: {carpeta}")
        else:
            print(f"❌ Falta: {carpeta}")

if __name__ == "__main__":
    verificar_carpetas()
