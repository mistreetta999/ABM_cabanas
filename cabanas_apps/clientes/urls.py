"""urls.py de la app clientes"""
from django.urls import path

import django_core
from . import views

app_name = "clientes"

urlpatterns = [
    # Rutas específicas de la app clientes (rutas generales temporales para evitar imports a módulos inexistentes)
    path("interfaz_gestion_cabanas/", views.lista_clientes, name="lista_clientes"),
    path("", views.lista_clientes, name="lista_clientes"),
    path("home/", views.ClientesHomeView.as_view(), name="home"),
    path("clientes/<int:pk>/", views.ClienteDetailView.as_view(), name="detalle_cliente"),
    path("clientes/<int:pk>/editar/", views.ClienteUpdateView.as_view(), name="editar_cliente"),
    path("clientes/<int:pk>/eliminar/", views.ClienteDeleteView.as_view(), name="eliminar_cliente"),
]
