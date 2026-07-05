from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('cabanas_apps.reservas.urls')),
    path('cabanas/', include('cabanas_apps.cabanas.urls')),
    path('gestion/', include('cabanas_apps.gestion_cabanas.urls')),
    path('clientes/', include('cabanas_apps.clientes.urls')),
    path('', include('cabanas_api.urls')),  # si tu API tiene urls propias
]
