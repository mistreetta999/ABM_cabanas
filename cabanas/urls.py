"""URL configuration for cabanas project.  """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # App principal API
    path('', include('cabanas_api.urls')),  # corregido: siempre cabanas_api

    # Apps internas
    path('reservas/', include('cabanas_apps.reservas.urls')),
    path('pagos/', include('cabanas_apps.pagos.urls')),
    path('alquileres/', include('cabanas_apps.alquileres.urls')),
    path('clientes/', include('cabanas_apps.clientes.urls')),
    path('registros/', include('cabanas_apps.registros.urls')),
]
