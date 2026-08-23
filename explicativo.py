"""para explicar la estructura del proyecto Django de cabañas"""
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URLS_FILE = "urls.py"
APP_FILES = ["models.py", "views.py", URLS_FILE, "admin.py"]

estructura = {
    "django_core": {
        "descripcion": "Núcleo del proyecto (settings.py, urls.py, wsgi.py, asgi.py)",
        "archivos": ["settings.py", "urls.py", "wsgi.py", "asgi.py"]
    },
    "cabanas_apps_django/usuarios": {
        "descripcion": "Gestión de usuarios y autenticación",
        "archivos": APP_FILES
    },
    "cabanas_apps_django/clientes": {
        "descripcion": "Módulo de clientes y sus datos",
        "archivos": APP_FILES
    },
    "cabanas_apps_django/alquileres": {
        "descripcion": "Reservas y alquileres de cabañas",
        "archivos": APP_FILES
    },
    "cabanas_apps_django/cabanas": {
        "descripcion": "Modelos y lógica de las cabañas",
        "archivos": APP_FILES
    },
    "cabanas_apps_django/facturas": {
        "descripcion": "Facturación y administración de pagos",
        "archivos": APP_FILES
    },
    "templates": {
        "descripcion": "Plantillas HTML para las vistas",
        "archivos": []
    },
    "static": {
        "descripcion": "Archivos estáticos (CSS, JS, imágenes)",
        "archivos": []
    }
}

def comprobar_estructura():
    """"def comprobar estructura del proyecto Django"""
    print(f"\n📂 Proyecto Django en: {BASE_DIR}\n")
    for carpeta, datos in estructura.items():
        ruta = os.path.join(BASE_DIR, carpeta)
        existe = "✅" if os.path.exists(ruta) else "❌"
        print(f"{existe} {carpeta} → {datos['descripcion']}")
        for archivo in datos["archivos"]:
            ruta_archivo = os.path.join(ruta, archivo)
            existe_archivo = "✅" if os.path.exists(ruta_archivo) else "❌"
            print(f"   {existe_archivo} {archivo}")
        print()

if __name__ == "__main__":
    comprobar_estructura()


def mostrar_estructura(base_dir):
    """función para mostrar la estructura del proyecto Django"""
    print(f"\n📂 Proyecto Django en: {base_dir}\n")
    carpetas = {
        "django_core": "Núcleo del proyecto (settings.py, urls.py, wsgi.py, asgi.py)",
        "cabanas_apps_django/usuarios": "Gestión de usuarios y autenticación",
        "cabanas_apps_django/clientes": "Módulo de clientes y sus datos",
        "cabanas_apps_django/alquileres": "Reservas y alquileres de cabañas",
        "cabanas_apps_django/cabanas": "Modelos y lógica de las cabañas",
        "cabanas_apps_django/facturas": "Facturación y administración de pagos",
        "templates": "Plantillas HTML para las vistas",
        "static": "Archivos estáticos (CSS, JS, imágenes)",
    }

    for carpeta, descripcion in carpetas.items():
        ruta = os.path.join(base_dir, carpeta)
        existe = "✅" if os.path.exists(ruta) else "❌"
        print(f"{existe} {carpeta} → {descripcion}")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    mostrar_estructura(BASE_DIR)
