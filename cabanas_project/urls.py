"""URLs raíz del proyecto cabanas_project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path("admin/", admin.site.urls),

    # Rutas principales de todas las apps
    path("", include("web.urls")),  # Página pública principal
    path("cabanas_apps/", include("cabanas_apps.urls")),  # Router central de apps internas
]
