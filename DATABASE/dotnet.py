"""Conexión simple a SQLite estilo .NET"""

import os
import sqlite3
from pathlib import Path

# Ruta de la base de datos (por defecto en la carpeta del proyecto)
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = os.getenv("DB_PATH", BASE_DIR / "db.sqlite3")


def get_connection():
    """Devuelve una conexión a SQLite"""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except Exception as e:
        raise RuntimeError(f"Error al conectar a la base de datos: {e}") from e


def execute_query(query, params=None):
    """Ejecuta una consulta SELECT y devuelve resultados"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or [])
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def execute_non_query(query, params=None):
    """Ejecuta un INSERT/UPDATE/DELETE"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or [])
    conn.commit()
    cursor.close()
    conn.close()
