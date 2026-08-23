from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alquiler, Cabana, Cliente, Registro, Reserva

# --- ALQUILERES ---
class AlquilerCreateView(CreateView):
    model = Alquiler
    fields = "__all__"
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")

class AlquilerListView(ListView):
    model = Alquiler
    template_name = "alquileres/list.html"
    context_object_name = "alquileres"

class AlquilerUpdateView(UpdateView):
    model = Alquiler
    fields = "__all__"
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")

class AlquilerDeleteView(DeleteView):
    model = Alquiler
    template_name = "alquileres/confirm_delete.html"
    success_url = reverse_lazy("alquiler_list")


# --- CABAÑAS ---
class CabanaCreateView(CreateView):
    model = Cabana
    fields = "__all__"
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/list.html"
    context_object_name = "cabanas"

class CabanaUpdateView(UpdateView):
    model = Cabana
    fields = "__all__"
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")

class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabana_list")


# --- CLIENTES ---
class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "clientes/form.html"
    success_url = reverse_lazy("cliente_list")

class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/list.html"
    context_object_name = "clientes"

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"
    template_name = "clientes/form.html"
    success_url = reverse_lazy("cliente_list")

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/confirm_delete.html"
    success_url = reverse_lazy("cliente_list")


# --- REGISTROS ---
class RegistroCreateView(CreateView):
    model = Registro
    fields = "__all__"
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")

class RegistroListView(ListView):
    model = Registro
    template_name = "registros/list.html"
    context_object_name = "registros"

class RegistroUpdateView(UpdateView):
    model = Registro
    fields = "__all__"
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")

class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = "registros/confirm_delete.html"
    success_url = reverse_lazy("registro_list")


# --- RESERVAS ---
class ReservaCreateView(CreateView):
    model = Reserva
    fields = "__all__"
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")

class ReservaListView(ListView):
    model = Reserva
    template_name = "reservas/list.html"
    context_object_name = "reservas"

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = "__all__"
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "reservas/confirm_delete.html"
    success_url = reverse_lazy("reserva_list")
