"""URL configuration for cabanas project.  """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # App principal API
    path('', include('cabana_api.urls')),  

    # Apps internas
    path('reservas/', include('cabana_apps.reservas.urls')),
    path('clientes/', include('cabana_apps.clientes.urls')),
    path('registros/', include('cabana_apps.registros.urls')),
]
