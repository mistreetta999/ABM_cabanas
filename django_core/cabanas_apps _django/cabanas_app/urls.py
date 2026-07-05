"""URL configuration for cabanas_apps project."""
from django.urls import path
from django.urls import include

APP_NAME = "cabanas"

urlpatterns = [
    path('', include('cabanas_api.urls')),
    path('admin/', include('cabanas_api.urls')),  # si tu API tiene urls propias
    path('reservas/', include('cabanas_apps.reservas.urls')),
    path('cabanas/', include('cabanas_apps.cabanas.urls')),
    path('gestion/', include('cabanas_apps.gestion_cabanas.urls')),
    path('clientes/', include('cabanas_apps.clientes.urls')),
    path('interfaz/', include('cabanas_apps.interfaz_gestion_cabanas.urls')),
    path('alquileres/', include('cabanas_apps.alquileres.urls')),
    path('pagos/', include('cabanas_apps.pagos.urls')),
    path('registros/', include('cabanas_apps.registros.urls')),
]
