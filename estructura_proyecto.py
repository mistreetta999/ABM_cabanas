
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

estructura = {
    "django_core": "Núcleo del proyecto (settings.py, urls.py, wsgi.py, asgi.py)",
    "cabanas_apps_django/usuarios": "Gestión de usuarios y autenticación",
    "cabanas_apps_django/clientes": "Módulo de clientes y sus datos",
    "cabanas_apps_django/alquileres": " alquileres de cabañas",
    "cabanas_apps_django/reservas": "Reservas de cabañas",
    "cabanas_apps_django/cabanas": "Modelos y lógica de las cabañas",
    "cabanas_apps_django/facturas": "Facturación y administración de pagos",
    "cabanas_apps_django/registros": "Registro de actividades y transacciones",
    "templates": "Plantillas HTML para las vistas",
    "static": "Archivos estáticos (CSS, JS, imágenes)",
}

def comprobar_estructura():
    """Comprueba la existencia de las carpetas principales del proyecto."""
    print(f"\n📂 Proyecto Django en: {BASE_DIR}\n")
    for carpeta, descripcion in estructura.items():
        ruta = os.path.join(BASE_DIR, carpeta)
        existe = "✅" if os.path.exists(ruta) else "❌"
        print(f"{existe} {carpeta} → {descripcion}")

if __name__ == "__main__":
    comprobar_estructura()
