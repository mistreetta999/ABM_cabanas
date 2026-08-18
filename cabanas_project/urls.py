"""Archivo de configuracion de URLs del proyecto Cabanas."""
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpRequest, HttpResponse
from django.urls import include, path
from django.shortcuts import render

app_name = "cabanas_project"

def pagina_principal(request):
    """Renderiza la página principal"""
    return render(request, "pagina_principal.html")

urlpatterns = [
    path("", pagina_principal, name="pagina_principal"),
]

def robots_txt(request: HttpRequest) -> HttpResponse:
    """Genera el archivo robots.txt dinámicamente."""
    sitemap_url = request.build_absolute_uri("/sitemap.xml")
    content = f"""User-agent: *
Disallow: /interfaz_gestion_cabanas/

Sitemap: {sitemap_url}
"""
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request: HttpRequest) -> HttpResponse:
    """Genera el archivo sitemap.xml dinámicamente."""
    base_url = request.build_absolute_uri("/").rstrip("/")
    urls = [
        ("", "weekly", "1.0"),
        ("cabanas/", "weekly", "0.9"),
        ("alquileres/", "weekly", "0.7"),
        ("pagos/", "monthly", "0.6"),
        ("chatbot/", "monthly", "0.5"),
        ("reservas/", "weekly", "0.8"),
        ("clientes/", "monthly", "0.6"),
        ("registros/", "monthly", "0.5"),
        ("usuarios/", "monthly", "0.6"),
        ("DATABASE/", "monthly", "0.9"),
        ("pagina_principal/", "weekly", "0.7"),
        ("interfaz_getion_cabanas/", "weekly", "0.1"),
        ("getion_cabanas/", "weekly", "0.11"),
        ("robots.txt", "monthly", "0.2"),
        ("web/", "monthly", "0.3"),
        ("interfaz_gestion_cabanas/", "monthly", "0.10"),
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for path_url, freq, priority in urls:
        xml += f"""  <url>
    <loc>{base_url}/{path_url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""
    xml += "</urlset>"
    return HttpResponse(xml, content_type="application/xml")


urlpatterns = [
    path("robots.txt", robots_txt),
    path("sitemap.xml", sitemap_xml),
    path("pagina_principal.html/", pagina_principal, name="pagina_principal_html"),
    path("pagina_principal.html", pagina_principal, name="pagina_principal_html_sin_barra"),

    # Rutas de tus aplicaciones
    path("DATABASE/", include("DATABASE.urls")),
    path("cabanas_principal/", include("cabanas_principal.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("web/", include("web.urls")),
    path("", include("cabanas_apps.gestion_cabanas.urls")),
# REMOVED usuarios_sistema
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
