""" archivo de vistas de la app pagos

"""
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from .models import Pago

class PagoView(ListView):
    """ Vista para ver los pagos """
    model = Pago
    template_name = "pagos/list.html"
    context_object_name = "pagos"   

class PagoListView(ListView):
    """ Vista para listar los pagos """
    model = Pago
    template_name = "pagos/list.html"
    context_object_name = "pagos"
class PagoCreateView(CreateView):
    """ Vista para crear un nuevo pago """
    model = Pago
    template_name = "pagos/create.html"
    fields = ['reserva', 'monto', 'fecha_pago']
    success_url = reverse_lazy('pago_list')
    
class PagoUpdateView(UpdateView):
    """ Vista para actualizar un pago existente """
    model = Pago
    template_name = "pagos/update.html"
    fields = ['reserva', 'monto', 'fecha_pago']
    success_url = reverse_lazy('pago_list')
class PagoDeleteView(DeleteView):
    """ Vista para eliminar un pago existente """
    model = Pago
    template_name = "pagos/delete.html"
    success_url = reverse_lazy('pago_list') 
class PagoDetailView(DetailView):
    """ Vista para mostrar los detalles de un pago """
    model = Pago
    template_name = "pagos/detail.html"
    context_object_name = "pago"
    
