"""URLs locales del sistema de cabanas."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.urls import include, path
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.contrib import admin
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.urls import path
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django_local import views
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.urls.resolvers import _URLConf
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from typing import Any
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from . import views
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
app_name = "django_local"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def include(
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
 arg: _URLConf:Any | tuple[_URLConf, str],
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
 namespace: str | None = None
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
) -> _IncludedURLConf
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
urlpatterns = [
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path('admin/', admin.site.urls),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path('principal/', views.pagina_principal, name='pagina_principal'),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("pagina_principal", views.PaginaPrincipalViews, name="pagina_principal.html"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("panel/", views.panel_django, name="panel_django.dj"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("clientes/", views.cliente_list, name="cliente_list"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("clientes/nuevo/", views.cliente_create, name="cliente_create"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("clientes/<int:pk>/editar/", views.cliente_edit, name="cliente_edit"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("clientes/<int:pk>/borrar/", views.cliente_delete, name="cliente_delete"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("reservas/", views.reserva_list, name="reserva_list"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("reservas/nuevo/", views.reserva_create, name="reserva_create"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("alquileres/", views.alquiler_list, name="alquiler_list"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("alquileres/nuevo/", views.alquiler_create, name="alquiler_create"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("pagos/", views.pago_list, name="pago_list"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("pagos/nuevo/", views.pago_create, name="pago_create"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("registros/", views.registro_list, name="registro_list"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    path("registros/nuevo/", views.registro_create, name="registro_create"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
]
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
