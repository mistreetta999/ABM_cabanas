""""este archivo contiene las urls de la app registros"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),

    # Home / panel principal
    path("", include("cabanas_apps.urls")),

    # Chatbot
    path("chatbot/", include("chatbot.urls")),

    # Módulos internos
    path("reservas/", include("cabanas_apps.reservas_alquileres_apps.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),

    # App principal de Cabanas
    path("cabanas/", include("cabanas.urls")),
]
