""" views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from django_core.cabanas_apps_django.registros.models import Registro
from .forms import RegistroForm


# --- API REST ---
class RegistroViewSet(viewsets.ModelViewSet):
    """API REST para gestionar registros."""
    queryset = Registro.objects.all()  # pylint: disable=no-member
    serializer_class = None  # ⚠️ reemplazar con tu serializer (ej: RegistroSerializer)


# --- Vistas HTML ---
class ListaRegistrosView(ListView):
    """Vista para listar todos los registros."""
    model = Registro
    template_name = "registros/lista.html"
    context_object_name = "registros"


class DetalleRegistroView(DetailView):
    """Vista para mostrar el detalle de un registro."""
    model = Registro
    template_name = "registros/detalle.html"
    context_object_name = "registro"


class CrearRegistroView(View):
    """Vista para crear un nuevo registro."""
    def get(self, request):
        """Renderiza el formulario para crear un nuevo registro."""
        form = RegistroForm()
        return render(request, "registros/formulario.html", {"form": form})

    def post(self, request):
        """Procesa el formulario para crear un nuevo registro."""
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_registros")
        return render(request, "registros/formulario.html", {"form": form})


class EditarRegistroView(View):
    """Vista para editar un registro existente."""
    def get(self, request, pk):
        """Renderiza el formulario para editar un registro existente."""
        registro = get_object_or_404(Registro, pk=pk)
        form = RegistroForm(instance=registro)
        return render(request, "registros/formulario.html", {"form": form})

    def post(self, request, pk):
        """Procesa el formulario para editar un registro existente."""
        registro = get_object_or_404(Registro, pk=pk)
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect("lista_registros")
        return render(request, "registros/formulario.html", {"form": form})


class EliminarRegistroView(View):
    """Vista para eliminar un registro existente."""
    def get(self, request, pk):
        """Renderiza la página de confirmación para eliminar un registro existente."""
        registro = get_object_or_404(Registro, pk=pk)
        return render(request, "registros/confirmar_eliminar.html", {"registro": registro})

    def post(self, _request, pk):
        """Elimina el registro existente después de la confirmación."""
        registro = get_object_or_404(Registro, pk=pk)
        registro.delete()
        return redirect("lista_registros")
