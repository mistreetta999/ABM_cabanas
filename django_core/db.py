"""Módulo de utilidad para la gestión de la base de datos."""

from django.conf import settings
from django.db import connections, DEFAULT_DB_ALIAS

class Database:
    """
    Clase auxiliar para manejar la conexión a la base de datos
    en el proyecto de Gestión de Cabañas.
    """

    def __init__(self, alias=DEFAULT_DB_ALIAS):
        self.alias = alias
        self.connection = connections[self.alias]

    def get_cursor(self):
        """
        Devuelve un cursor para ejecutar consultas SQL.
        """
        return self.connection.cursor()

    def execute(self, query, params=None):
        """
        Ejecuta una consulta SQL con parámetros opcionales.
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params or [])
            return cursor.fetchall()

    def commit(self):
        """
        Confirma los cambios en la base de datos.
        """
        self.connection.commit()

    def close(self):
        """
        Cierra la conexión activa.
        """
        self.connection.close()
