""" views de la app registros
"""
from django.views.generic import ListView
from .models import ActividadCabanas



class ActividadCabanasListView(ListView):
    """Vista para listar las actividades de las cabañas."""
    model = ActividadCabanas
    template_name = "registros/lista.html"
    context_object_name = "actividades"
    paginate_by = 10

    def get_queryset(self):
        """Obtiene actividades ordenadas por fecha descendente."""
        return super().get_queryset().order_by("-fecha")

    def get(self, request, *args, **kwargs):
        print("Vista de Registros")
        return super().get(request, *args, **kwargs)
    print("Vista de Registros")
