"""URLs principales del proyecto config."""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    # API principal
    path("api/", include("cabanas_api.urls")),

    # Apps activas
    path("pagina_principal.html", TemplateView.as_view(template_name="pagina_principal.html"), name="pagina_principal_html_sin_barra"),

    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("web/", include("django_core.cabanas_apps_django.web.urls")),
    path("chatbot/", include("django_core.cabanas_apps_django.chatbot_app.urls")),
]
