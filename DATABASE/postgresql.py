"""
Configuración de conexión a PostgreSQL
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gestion_cabanas",   # Nombre de la base de datos
        "USER": "postgres",          # Usuario de PostgreSQL
        "PASSWORD": "tu_password",   # Contraseña
        "HOST": "localhost",         # Servidor
        "PORT": "5432",              # Puerto por defecto
    }
}
