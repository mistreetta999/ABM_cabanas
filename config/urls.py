"""URLs principales del proyecto config."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API principal
    path("api/", include("cabanas_api.urls")),

    # Apps activas
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("web/", include("django_core.cabanas_apps_django.web.urls")),
    path("chatbot/", include("django_core.cabanas_apps_django.chatbot_app.urls")),
]
