"""URLs de la aplicación Web, integradas con el sistema."""

from django.urls import path, include

app_name = "web"  # pylint: disable=invalid-name

urlpatterns = [
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
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
]
