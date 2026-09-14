"""Conexión a PostgreSQL para el proyecto de cabañas."""
import os
import psycopg2
from psycopg2 import sql

# Configuración de conexión (puede venir de variables de entorno .env)
DB_NAME = os.getenv("DB_NAME", "cabanas_db")
DB_USER = os.getenv("DB_USER", "carolina")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_connection():
    """Devuelve una conexión activa a PostgreSQL."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        return conn
    except Exception as e:
        raise RuntimeError(f"Error al conectar con PostgreSQL: {e}") from e

def execute_query(query, params=None):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql.SQL(query), params or [])
            if cur.description:  # si la consulta devuelve datos
                return cur.fetchall()
            conn.commit()
    finally:
        conn.close()

def init_test():
    """Prueba rápida de conexión."""
    rows = execute_query("SELECT version();")
    return rows[0][0] if rows else "Sin respuesta"
