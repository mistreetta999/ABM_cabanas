"""
Vistas de la aplicación Registros.
Permite consultar y visualizar el historial de eventos del sistema.
"""

from django.views.generic import ListView, DetailView
from .models import Registro


class RegistroListView(ListView):
    """Lista todos los registros del sistema."""
    model = Registro
    template_name = "registros/registro_list.html"
    context_object_name = "registros"
    paginate_by = 20  # Paginación para no sobrecargar la vista

    def get_queryset(self):
        """
        Permite filtrar registros por tipo si se pasa un parámetro en la URL.
        Ejemplo: /registros/?tipo=pago
        """
        queryset = super().get_queryset()
        tipo = self.request.GET.get("tipo")
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        return queryset


class RegistroDetailView(DetailView):
    """Muestra el detalle de un registro específico."""
    model = Registro
    template_name = "registros/registro_detail.html"
    context_object_name = "registro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registro = self.get_object()
        # Agregamos un resumen legible para mostrar en la plantilla
        context["resumen"] = registro.resumen()
        return context
