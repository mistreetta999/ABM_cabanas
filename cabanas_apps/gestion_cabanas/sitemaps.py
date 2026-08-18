from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Cabanas
, Reservas, Alquiler, Pago

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["index", "chatbot"]

    def location(self, item):
        return reverse(item)


class CabanaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Cabanas
.objects.all()

    def lastmod(self, obj):
        return obj.id  # si tenés campo fecha_modificación, usalo aquí


class AlquilerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Alquiler.objects.all()


class PagoSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Pago.objects.all()
