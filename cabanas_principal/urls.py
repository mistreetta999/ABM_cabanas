

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rutas habilitadas: clientes, alquileres
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
]
