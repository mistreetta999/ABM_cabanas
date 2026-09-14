"""Vistas de la aplicación Public."""
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class HomeView(View):
    """Vista de la página de inicio en texto plano."""
    def get(self, _request):
        """Devuelve la página de inicio en texto plano."""
        return HttpResponse("Bienvenida a Alquileres Cabañas")

class AcercaDeView(View):
    """Vista de la página 'Acerca de nosotros' en texto plano."""
    def get(self, _request):
        """Devuelve la página 'Acerca de nosotros' en texto plano."""
        return HttpResponse("Acerca de nosotros")

class ContactoView(View):
    """Vista de la página de contacto en texto plano."""
    def get(self, _request):
        """Devuelve la página de contacto en texto plano."""
        return HttpResponse("Página de contacto")

# Si querés usar templates en lugar de texto plano:
class HomeTemplateView(View):
    """Vista de la página de inicio usando template."""
    def get(self, request):
        """Devuelve la página de inicio usando template."""
        return render(request, "public/home.html")

class AcercaDeTemplateView(View):
    """Vista de la página 'Acerca de nosotros' usando template."""
    def get(self, request):
        """Devuelve la página 'Acerca de nosotros' usando template."""
        return render(request, "public/acerca_de.html")

class ContactoTemplateView(View):
    """Vista de la página de contacto usando template."""
    def get(self, request):
        """Devuelve la página de contacto usando template."""
        return render(request, "public/contacto.html")
