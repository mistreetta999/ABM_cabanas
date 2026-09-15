"""URLs de la aplicación Web, integradas con el sistema."""

from django.urls import include, path
from django_core.cabanas_apps_django.web.views import dashboard_interactivo
from .views import (
    WebContactView,
    WebHelpView,
    WebInfoView,
    cabanas_list,
    clientes_list,
    home,
    pagos_list,
    reservas_list,
)

app_name = "web"  # pylint: disable=invalid-name

urlpatterns = [
    path('dashboard/', dashboard_interactivo, name='dashboard_interactivo'),
    # Rutas de vistas generales del sitio web
    path("info/", WebInfoView.as_view(), name="web_info"),
    path("contact/", WebContactView.as_view(), name="web_contact"),
    path("help/", WebHelpView.as_view(), name="web_help"),
    # Rutas principales de la aplicación html
    path("", home, name="home"),
    path("clientes/", clientes_list, name="clientes_list"),
    path("reservas/", reservas_list, name="reservas_list"),
    path("cabanas/", cabanas_list, name="cabanas_list"),
    path("pagos/", pagos_list, name="pagos_list"),
    # Páginas principales del sitio web
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("chatbot/", include("django_core.cabanas_apps_django.chatbot_app.urls")),
    path("web/", include("django_core.cabanas_apps_django.web.urls")),
    # Ejemplo de ruta raíz
    path("", include("django_core.cabanas_apps_django.web.urls")),
    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),  # relación con cabañas
    path("alquileres/", include("alquileres.urls")),  # relación con alquileres
    path("reservas/", include("reservas.urls")),  # relación con reservas
    path("clientes/", include("clientes.urls")),  # relación con clientes
    path("facturas/", include("facturas.urls")),  # relación con facturas
    path("pagos/", include("pagos.urls")),  # relación con pagos
    path("usuarios/", include("usuarios.urls")),  # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),  # relación con chatbot
    path(
        "gestion/", include("gestion_cabanas.urls")
    ),  # relación con gestión de cabañas
    path(
        "interfaz/", include("interfaz_gestion_cabanas.urls")
    ),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),  # relación con registros
]
