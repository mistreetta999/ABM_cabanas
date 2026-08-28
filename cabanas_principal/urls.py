""" urls"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="pagina_principal.html"), name="home"),

    # Apps montadas como rutas reales del proyecto
    path("alquileres/", TemplateView.as_view(template_name="pagina_principal.html"), name="alquileres"),
    path("cabanas/", TemplateView.as_view(template_name="pagina_principal.html"), name="cabanas"),
    path("clientes/", TemplateView.as_view(template_name="pagina_principal.html"), name="clientes"),
    path("reservas/", TemplateView.as_view(template_name="pagina_principal.html"), name="reservas"),
    path("registros/", TemplateView.as_view(template_name="pagina_principal.html"), name="registros"),
    path("usuarios/", TemplateView.as_view(template_name="pagina_principal.html"), name="usuarios"),
    path("pagos/", TemplateView.as_view(template_name="pagina_principal.html"), name="pagos"),
    path("facturas/", TemplateView.as_view(template_name="pagina_principal.html"), name="facturas"),
    path("gestion/", TemplateView.as_view(template_name="pagina_principal.html"), name="gestion"),
    path("interfaz/", TemplateView.as_view(template_name="pagina_principal.html"), name="interfaz"),
    path("web/", TemplateView.as_view(template_name="pagina_principal.html"), name="web"),
    path("chatbot/", TemplateView.as_view(template_name="pagina_principal.html"), name="chatbot"),
]
