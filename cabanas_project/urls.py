from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def robots_txt(request):
    sitemap_url = request.build_absolute_uri("/sitemap.xml")
    content = f"""User-agent: *
Disallow:

Sitemap: {sitemap_url}
"""
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    base_url = request.build_absolute_uri("/").rstrip("/")
    urls = [
        ("", "weekly", "1.0"),
        ("cabanas/", "weekly", "0.9"),
        ("alquileres/", "weekly", "0.7"),
        ("pagos/", "monthly", "0.6"),
        ("chatbot/", "monthly", "0.5"),
    ]
    entries = "\n".join(
        f"""  <url>
    <loc>{base_url}/{path}</loc>
    <lastmod>2026-05-21</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
        for path, changefreq, priority in urls
    )
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    return HttpResponse(content, content_type="application/xml")


urlpatterns = [
    path("robots.txt", robots_txt),
    path("sitemap.xml", sitemap_xml),
    path("", include("cabanas_apps.urls")),
    path("chatbot/", include("chatbot.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
