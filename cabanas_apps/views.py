""" Vistas de la aplicación Cabañas."""
from pathlib import Path

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from .models import Cliente, Cabanas
, Reserva, Alquiler, Registro


BASE_DIR = Path(__file__).resolve().parent.parent
# cabanas_apps/interfaz_gestion_cabanas/views.py
from django.http import JsonResponse

def Cabanas
(request):
    return JsonResponse({"vista": "Cabanas
 funcionando"})

def Alquileres(request):
    return JsonResponse({"vista": "Alquileres funcionando"})

def Usuarios(request):
    return JsonResponse({"vista": "Usuarios funcionando"})

def Reservas(request):
    return JsonResponse({"vista": "Reservas funcionando"})

def Pagos(request):
    return JsonResponse({"vista": "Pagos funcionando"})

def Registros(request):
    return JsonResponse({"vista": "Registros funcionando"})

def Chatbot(request):
    return JsonResponse({"vista": "Chatbot funcionando"})

def Clientes(request):
    return JsonResponse({"vista": "Clientes funcionando"})

def pagina_principal(request):
    """ Vista para la página principal """
    return render(request, "pagina_principal.html")


class InicioView(TemplateView):
    """ Vista para la página de pagina_principal """
    template_name = "pagina_principal.html"


class PanelView(TemplateView):
    """ Vista para el panel genérico """
    template_name = "panel.html"


class ViewsModels:
    """"vista completa de models"""
    ViewsModels = models
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


class CabanaListView(ListView):
    """ Vista para listar las cabañas """
    model = Cabanas

    template_name = "cabanas/list.html"


class CabanaCreateView(CreateView):
    """ Vista para crear una nueva cabaña """
    model = Cabanas

    fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")


class CabanaUpdateView(UpdateView):
    """ Vista para actualizar una cabaña existente """
    model = Cabanas

    fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]
    template_name = "cabanas/form.html"
    success_url = reverse_lazy("cabana_list")


class CabanaDeleteView(DeleteView):
    """ Vista para eliminar una cabaña existente """
    model = Cabanas

    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabana_list")


# Reservas
class ReservaListView(ListView):
    """ Vista para listar las reservas """
    model = Reserva
    template_name = "reservas/list.html"


class ReservaCreateView(CreateView):
    """ Vista para crear una nueva reserva """
    model = Reserva
    fields = ["Cabanas
", "cliente", "fecha_inicio", "fecha_fin", "estado"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")


class ReservaUpdateView(UpdateView):
    """ Vista para actualizar una reserva existente """
    model = Reserva
    fields = ["Cabanas
", "cliente", "fecha_inicio", "fecha_fin", "estado"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reserva_list")


class ReservaDeleteView(DeleteView):
    """ Vista para eliminar una reserva existente """
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
    fields = ["Cabanas
", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]
    template_name = "alquileres/form.html"
    success_url = reverse_lazy("alquiler_list")


class AlquilerUpdateView(UpdateView):
    """ Vista para actualizar un alquiler existente """
    model = Alquiler
    fields = ["Cabanas
", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]
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
    """ Vista para actualizar un registro """
    model = Registro
    fields = ["reserva", "cliente", "detalle"]
    template_name = "registros/form.html"
    success_url = reverse_lazy("registro_list")


class RegistroDeleteView(DeleteView):
    """ Vista para eliminar un registro existente """
    model = Registro
    template_name = "registros/confirm_delete.html"
    success_url = reverse_lazy("registro_list")
