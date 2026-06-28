"""URL configuration for cabanas project.  """
from django.contrib import admin
from django.urls import path, include
from cabanas_api.views import pagina_principal, gestion
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_principal, name='pagina_principal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # aquí siguen las demás apps
    path("admin/", admin.site.urls),
    path("pagina_principal/", pagina_principal, name="pagina_principal"),
    path("gestion/", gestion, name="gestion"),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
]
