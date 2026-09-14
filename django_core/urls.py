"""URLs Django relacionadas con las apps del sistema."""
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = "django_core"

urlpatterns = [
    path("pagina_principal.html", TemplateView.as_view(template_name="pagina_principal.html"), name="pagina_principal"),
    path("render/", include("django_core.render_support.urls")),
    path("api/", include("cabanas_api.urls")),
    path("apps/", include("cabanas_apps.urls")),
    path("django_local/", include("django_local.urls")),
    path("templates/", include("Templates.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("cabanas-app/", include("cabanas_apps.cabanas_app.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("facturas/", include("cabanas_apps.facturas.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("web/", include("web.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
