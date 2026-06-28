"""URL configuration for cabanas project.  """
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('cabanas_api.urls')),
    path("apps/", include("cabanas_apps.urls")),
    path("api/", include("cabanas_api.urls")),
    path("gestion/", views.gestion, name="gestion"),
    path('admin/', admin.site.urls),
    path('', include('cabanas_api.urls')),  # o cabanas_aps
    path('chatbot/', include('chatbot_app.urls')),  # chatbot
    path('', views.pagina_principal, name='pagina_principal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("pagina_principal/", views.pagina_principal, name="pagina_principal"),
    path("gestion/", views.gestion, name="gestion"),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("admin/", admin.site.urls),
    path("apps/", include("cabanas_apps.urls")),
    path("api/", include("cabanas_api.urls")),
    path("gestion/", include("cabanas_apps.gestion.urls")),
]
