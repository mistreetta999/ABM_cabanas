"""Django URL Configuration"""
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", include("cabanas_principal.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
]


# Configuracion de la URL para la documentacion de la API (Swagger)
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]

