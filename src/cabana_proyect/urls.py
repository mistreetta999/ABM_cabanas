"""URLs raíz del proyecto cabana_proyect."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Panel de administración de Django
    path("admin/", admin.site.urls),
    # Rutas públicas
    path("", include("public.urls")),  # Página principal y secciones públicas
    # Rutas de apps internas
    path("django_local/", include("django_local.urls")),  # Gestión interna
    path("database/", include("DATABASE.urls")),  # Administración DB
    path("cabanas_apps/", include("cabanas_apps.urls")),  # Apps de cabañas
    # Chatbot público
    path("chatbot/", include("public.chatbot_app.urls")),
    path("chatbot/api/", include("public.chatbot_app.chatbot_api.urls")),
]
