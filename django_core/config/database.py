""" "database"""

from django.db import DEFAULT_DB_ALIAS, connections


def get_db_connection(alias=DEFAULT_DB_ALIAS):
    """Obtiene la conexión a la base de datos especificada por el alias."""
    return connections[alias]
