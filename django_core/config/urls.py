"""Django URL Configuration"""
from pathlib import Path
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reservas/", include("cabana_apps.reservas.urls")),
    path("clientes/", include("cabana_apps.clientes.urls")),
    path("registros/", include("cabana_apps.registros.urls")),
    path("cabanas/", include("cabanas.urls")),
]

# Configuración de la URL para la documentación de la API (Swagger)
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Configuración de la URL para la documentación de la API (Redoc)
urlpatterns += [
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
