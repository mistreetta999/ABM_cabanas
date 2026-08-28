"""
Vistas de la aplicación Reservas.
Permite gestionar reservas de cabañas vinculadas a clientes.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reserva


class ReservaListView(ListView):
    """Lista todas las reservas registradas."""
    model = Reserva
    template_name = "reservas/reserva_list.html"
    context_object_name = "reservas"
    paginate_by = 20

    def get_queryset(self):
        """
        Permite filtrar reservas por estado si se pasa un parámetro en la URL.
        Ejemplo: /reservas/?estado=pendiente
        """
        queryset = super().get_queryset()
        estado = self.request.GET.get("estado")
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset


class ReservaDetailView(DetailView):
    """Muestra el detalle de una reserva específica."""
    model = Reserva
    template_name = "reservas/reserva_detail.html"
    context_object_name = "reserva"


class ReservaCreateView(CreateView):
    """Permite registrar una nueva reserva."""
    model = Reserva
    template_name = "reservas/reserva_form.html"
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto_total"]
    success_url = reverse_lazy("reservas:reserva_list")

    def form_valid(self, form):
        # Validar que fecha_fin sea posterior a fecha_inicio
        if form.instance.fecha_fin < form.instance.fecha_inicio:
            form.add_error("fecha_fin", "La fecha de fin debe ser posterior a la fecha de inicio.")
            return self.form_invalid(form)
        return super().form_valid(form)


class ReservaUpdateView(UpdateView):
    """Permite editar una reserva existente."""
    model = Reserva
    template_name = "reservas/reserva_form.html"
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto_total", "estado"]
    success_url = reverse_lazy("reservas:reserva_list")


class ReservaDeleteView(DeleteView):
    """Permite eliminar una reserva."""
    model = Reserva
    template_name = "reservas/reserva_confirm_delete.html"
    success_url = reverse_lazy("reservas:reserva_list")
