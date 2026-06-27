from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models.cabana import Cabana
from .models.clientes import Cliente
from .models.reservas import Reserva
from .models.alquileres import Alquiler
from .models.registros import Registro

# Vista de inicio
class InicioView(TemplateView):
    template_name = "inicio.html"

# Panel genérico
class PanelView(TemplateView):
    template_name = "panel.html"

# Clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/list.html"

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ["nombre", "email", "telefono"]
    template_name = "clientes/form.html"
    success_url = reverse_lazy("cliente_list")

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ["nombre", "email", "telefono"]
    template_name = "clientes/form.html"
    success_url = reverse_lazy("cliente_list")

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/confirm_delete.html"
    success_url = reverse_lazy("cliente_list")

# Cabañas
class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/list.html"

class CabanaCreateView(CreateView):
    model = Cabana
    fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaUpdateView(UpdateView):
    model = Cabana
    fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabana_list")

# Reservas
class ReservaListView(ListView):
    model = Reserva
    template_name = "reservas/list.html"

class ReservaCreateView(CreateView):
    model = Reserva
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "estado"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "estado"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "reservas/confirm_delete.html"
    success_url = reverse_lazy("reserva_list")

# Alquileres
class AlquilerListView(ListView):
    model = Alquiler
    template_name = "alquileres/list.html"

class AlquilerCreateView(CreateView):
    model = Alquiler
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")

class AlquilerUpdateView(UpdateView):
    model = Alquiler
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")

class AlquilerDeleteView(DeleteView):
    model = Alquiler
    template_name = "alquileres/confirm_delete.html"
    success_url = reverse_lazy("alquiler_list")

# Registros
class RegistroListView(ListView):
    model = Registro
    template_name = "registros/list.html"

class RegistroCreateView(CreateView):
    model = Registro
    fields = ["reserva", "cliente", "detalle"]
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")

class RegistroUpdateView(UpdateView):
    model = Registro
    fields = ["reserva", "cliente", "detalle"]
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")

class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = "registros/confirm_delete.html"
    success_url = reverse_lazy("registro_list")
