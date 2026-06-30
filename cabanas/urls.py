"""URL configuration for cabanas project.  """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.contrib import admin
from django.shortcuts import render
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, CabanaSitemap, AlquilerSitemap, PagoSitemap

from cabanas_apps.gestion_cabanas.sitemaps import (AlquilerSitemap,
                                                   CabanaSitemap, PagoSitemap,
                                                   StaticViewSitemap)

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("panel/", views.panel_django, name="panel_django"),

    # Clientes
    path("clientes/", views.cliente_list, name="cliente_list"),
    path("clientes/nuevo/", views.cliente_create, name="cliente_create"),

    # Reservas
    path("reservas/", views.reserva_list, name="reserva_list"),
    path("reservas/nueva/", views.reserva_create, name="reserva_create"),

    # Alquileres
    path("alquileres/", views.alquiler_list, name="alquiler_list"),
    path("alquileres/nuevo/", views.alquiler_create, name="alquiler_create"),

    # Pagos
    path("pagos/", views.pago_list, name="pago_list"),
    path("pagos/nuevo/", views.pago_create, name="pago_create"),

    # Registros
    path("registros/", views.registro_list, name="registro_list"),
    path("registros/nuevo/", views.registro_create, name="registro_create"),
]




from . import views
def panel_django(request):
    return render(request, "panel_django.html")
def dashboard(request):
    return render(request, "dashboard.html")
def pagina_principal(request):
    return render(request, "pagina_principal.html")
def gestion(request):
    return render(request, "gestion.html")
def clientes(request):
    return render(request, "clientes.html")
def sitemap(request):
    return render(request, "sitemap.xml", content_type="application/xml")
sitemaps = {
    "static": StaticViewSitemap,
    "cabanas": CabanaSitemap,
    "alquileres": AlquilerSitemap,
    "pagos": PagoSitemap,
    
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("panel/", panel_django, name="panel_django"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("", include("cabanas_apps.gestion_cabanas.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
         name="django.contrib.sitemaps.views.sitemap"),

    path('', include('cabanas_api.urls')),
    path("pagina_principal/", views.pagina_principal, name="pagina_principal"),
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
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
