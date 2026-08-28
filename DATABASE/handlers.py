"""
Handlers para operaciones de base de datos.
Este módulo centraliza la lógica de backup, restore y consultas.
"""

import os
import subprocess
from django.db import connection
from django.core.exceptions import ValidationError


class DatabaseHandler:
    """Handler principal para operaciones sobre la base de datos."""

    @staticmethod
    def ejecutar_consulta(sql: str):
        """
        Ejecuta una consulta SQL directa y devuelve los resultados.
        ⚠️ Usar con precaución: no apto para queries no validadas.
        """
        with connection.cursor() as cursor:
            cursor.execute(sql)
            columnas = [col[0] for col in cursor.description] if cursor.description else []
            filas = cursor.fetchall() if cursor.description else []
        return {"columnas": columnas, "filas": filas}

    @staticmethod
    def backup(nombre_archivo: str = "backup.sql"):
        """
        Genera un respaldo de la base de datos en formato SQL.
        """
        try:
            comando = f"pg_dump {connection.settings_dict['NAME']} > {nombre_archivo}"
            subprocess.run(comando, shell=True, check=True)
            return f"Backup generado en {nombre_archivo}"
        except Exception as e:
            raise ValidationError(f"Error al generar backup: {e}")

    @staticmethod
    def restore(nombre_archivo: str = "backup.sql"):
        """
        Restaura la base de datos desde un archivo SQL.
        """
        if not os.path.exists(nombre_archivo):
            raise ValidationError("El archivo de respaldo no existe.")
        try:
            comando = f"psql {connection.settings_dict['NAME']} < {nombre_archivo}"
            subprocess.run(comando, shell=True, check=True)
            return f"Base restaurada desde {nombre_archivo}"
        except Exception as e:
            raise ValidationError(f"Error al restaurar base: {e}")

    @staticmethod
    def status():
        """
        Devuelve información básica del estado de la base de datos.
        """
        return {
            "engine": connection.settings_dict.get("ENGINE"),
            "name": connection.settings_dict.get("NAME"),
            "user": connection.settings_dict.get("USER"),
            "host": connection.settings_dict.get("HOST"),
            "port": connection.settings_dict.get("PORT"),
        }
