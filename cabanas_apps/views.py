""" Vistas de la aplicación Cabañas."""
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Cabana, Reserva, Alquiler, Registro

# Vista de inicio
class InicioView(TemplateView):
    """ Vista para la página de inicio """
    template_name = "inicio.html"

# Panel genérico
class PanelView(TemplateView):
    """ Vista para el panel genérico """
    template_name = "panel.html"

# Clientes
class ClienteListView(ListView):
    """ Vista para listar los clientes """
    model = Cliente
    template_name = "clientes/list.html"

class ClienteCreateView(CreateView):
    """ Vista para crear un nuevo cliente """   
    model = Cliente
    fields = ["nombre", "email", "telefono"]
    template_name = "clientes/form.html"
    success_url = reverse_lazy("cliente_list")

class ClienteUpdateView(UpdateView):
    """ Vista para actualizar un cliente existente """  
    model = Cliente
    fields = ["nombre", "email", "telefono"]
    template_name = "clientes/form.html"
    success_url = reverse_lazy("cliente_list")

class ClienteDeleteView(DeleteView):
    """ Vista para eliminar un cliente existente """  
    model = Cliente
    template_name = "clientes/confirm_delete.html"  
    success_url = reverse_lazy("cliente_list")

# Cabanas
class CabanaListView(ListView):
    """ Vista para listar las cabañas """
    model = Cabana
    template_name = "cabanas/list.html"

class CabanaCreateView(CreateView):
    """ Vista para crear una nueva cabaña """
    model = Cabana
    fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaUpdateView(UpdateView):
    """ Vista para actualizar una cabaña existente """
    model = Cabana
    fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaDeleteView(DeleteView):
    """ Vista para eliminar una cabaña existente """
    model = Cabana
    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabana_list")

# Reservas
class ReservaListView(ListView):
    """ Vista para listar las reservas """
    model = Reserva
    template_name = "reservas/list.html"

class ReservaCreateView(CreateView):
    
    
    model = Reserva
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "estado"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")

class ReservaUpdateView(UpdateView):
    """ Vista para actualizar una reserva existente """
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
    """ Vista para listar los alquileres """
    model = Alquiler
    template_name = "alquileres/list.html"

class AlquilerCreateView(CreateView):
    """ Vista para crear un nuevo alquiler """
    model = Alquiler
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")

class AlquilerUpdateView(UpdateView):
    """ Vista para actualizar un alquiler existente """
    model = Alquiler
    fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")

class AlquilerDeleteView(DeleteView):
    """ Vista para eliminar un alquiler existente """
    model = Alquiler
    template_name = "alquileres/confirm_delete.html"
    success_url = reverse_lazy("alquiler_list")

# Registros
class RegistroListView(ListView):
    """ Vista para listar los registros """
    model = Registro
    template_name = "registros/list.html"

class RegistroCreateView(CreateView):
    """ Vista para crear un nuevo registro """
    model = Registro
    fields = ["reserva", "cliente", "detalle"]
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")


class RegistroUpdateView(UpdateView):
    """ Vista para actualizar un registro existente """
    model = Registro
    fields = ["reserva", "cliente", "detalle"]
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")

class RegistroDeleteView(DeleteView):
    """ Vista para eliminar un registro existente """
    model = Registro
    template_name = "registros/confirm_delete.html"
    success_url = reverse_lazy("registro_list")
