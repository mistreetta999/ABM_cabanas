"""
Inicialización de la base de datos para el proyecto Cabañas.
"""

from django.db import connections, DEFAULT_DB_ALIAS, DatabaseError
from django.core.management import call_command, CommandError
from django.core.management.base import SystemCheckError


def init_database():
    """
    Ejecuta las migraciones iniciales para preparar la base de datos.
    """
    # Usar la conexión por defecto
    connection = connections[DEFAULT_DB_ALIAS]

    try:
        # Verificar conexión
        connection.ensure_connection()
        print("✅ Conexión a la base de datos establecida.")

        # Ejecutar migraciones
        call_command("makemigrations")
        call_command("migrate")
        print("✅ Migraciones aplicadas correctamente.")

    except (DatabaseError, CommandError, SystemCheckError) as e:
        print(f"❌ Error al inicializar la base de datos: {e}")


if __name__ == "__main__":
    init_database()
