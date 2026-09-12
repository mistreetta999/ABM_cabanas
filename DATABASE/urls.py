"""Rutas principales para la app DATABASE"""
from django.urls import path
from DATABASE import views

urlpatterns = [
    # Ejemplo: endpoint para probar conexión a la base de datos
    path("db/test/", views.test_connection, name="test_connection"),

    # Ejemplo: endpoint para listar clientes
    path("db/clientes/", views.list_clientes, name="list_clientes"),

    # Ejemplo: endpoint para crear un cliente
    path("db/clientes/nuevo/", views.create_cliente, name="create_cliente"),

    # Ejemplo: endpoint para reservas
    path("db/reservas/", views.list_reservas, name="list_reservas"),

]
