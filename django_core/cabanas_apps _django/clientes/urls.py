"""URL configuration para la app clientes."""
from django.urls import path

from .views import (
    ClienteCreateView,
    ClienteDeleteView,
    ClienteDetailView,
    ClienteListView,
    ClienteUpdateView,
    clientes_home,
)

app_name = "clientes"

urlpatterns = [
    path("", clientes_home, name="home"),
    path("lista/", ClienteListView.as_view(), name="lista"),
    path("nuevo/", ClienteCreateView.as_view(), name="crear"),
    path("<int:pk>/", ClienteDetailView.as_view(), name="detalle"),
    path("<int:pk>/editar/", ClienteUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", ClienteDeleteView.as_view(), name="eliminar"),
]
