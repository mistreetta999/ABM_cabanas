"""Vistas para la app DATABASE"""
from django.http import JsonResponse
from .db import get_connection, execute_query, execute_non_query

def test_connection(request):
    """Prueba la conexión a la base de datos"""
    try:
        conn = get_connection()
        conn.close()
        return JsonResponse({"status": "ok", "message": "Conexión exitosa"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

def list_clientes(request):
    """Lista todos los clientes"""
    try:
        results = execute_query("SELECT id, nombre, email FROM clientes")
        clientes = [{"id": r[0], "nombre": r[1], "email": r[2]} for r in results]
        return JsonResponse({"clientes": clientes})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

def create_cliente(request):
    """Crea un cliente de ejemplo"""
    try:
        execute_non_query(
            "INSERT INTO clientes (nombre, email) VALUES (?, ?)",
            ["Carolina", "carol@example.com"]
        )
        return JsonResponse({"status": "ok", "message": "Cliente creado"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

def list_reservas(request):
    """Lista todas las reservas"""
    try:
        results = execute_query("SELECT id, fecha, cliente_id FROM reservas")
        reservas = [{"id": r[0], "fecha": r[1], "cliente_id": r[2]} for r in results]
        return JsonResponse({"reservas": reservas})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
