"""urls.py de la app clientes, define las rutas para las vistas relacionadas con clientes, pagos y facturas."""
from django.urls import path
from . import views

APP_NAME = "clientes"

urlpatterns = [
    path("", views.lista_clientes, name="lista_clientes"),
    path("home/", views.ClientesHomeView.as_view(), name="home"),
    path("clientes/<int:pk>/", views.ClienteDetailView.as_view(), name="detalle_cliente"),
    path("clientes/<int:pk>/editar/", views.ClienteUpdateView.as_view(), name="editar_cliente"),
    path("clientes/<int:pk>/eliminar/", views.ClienteDeleteView.as_view(), name="eliminar_cliente"),
    path("clientes/nuevo/", views.ClienteCreateView.as_view(), name="nuevo_cliente"),
]
