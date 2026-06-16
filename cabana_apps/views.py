from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import AlquilerForm, CabanaForm, ClienteForm, PagoForm, RegistroForm, ReservaForm
from .models import Alquiler, Cabana, Cliente, Pago, Registro, Reserva


class InicioView(TemplateView):
    template_name = 'pagina_principal.html'


class PanelView(TemplateView):
    template_name = 'cabana_apps/panel_django.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes_count'] = Cliente.objects.count()
        context['reservas_count'] = Reserva.objects.count()
        context['alquileres_count'] = Alquiler.objects.count()
        context['pagos_count'] = Pago.objects.count()
        context['registros_count'] = Registro.objects.count()
        return context


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cabana_apps/list.html'
    context_object_name = 'objetos'
    extra_context = {'titulo': 'Clientes', 'crear_url': 'cliente_create', 'editar_url': 'cliente_update', 'borrar_url': 'cliente_delete'}


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Nuevo cliente'}


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Editar cliente'}


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cabana_apps/confirm_delete.html'
    success_url = '/abm/clientes/'


class CabanaListView(ListView):
    model = Cabana
    template_name = 'cabana_apps/list.html'
    context_object_name = 'objetos'
    extra_context = {'titulo': 'Cabanas', 'crear_url': 'cabana_create', 'editar_url': 'cabana_update', 'borrar_url': 'cabana_delete'}


class CabanaCreateView(CreateView):
    model = Cabana
    form_class = CabanaForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Nueva cabana'}


class CabanaUpdateView(UpdateView):
    model = Cabana
    form_class = CabanaForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Editar cabana'}


class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = 'cabana_apps/confirm_delete.html'
    success_url = '/abm/cabanas/'


class ReservaListView(ListView):
    model = Reserva
    template_name = 'cabana_apps/list.html'
    context_object_name = 'objetos'
    extra_context = {'titulo': 'Reservas', 'crear_url': 'reserva_create', 'editar_url': 'reserva_update', 'borrar_url': 'reserva_delete'}


class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Nueva reserva'}


class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Editar reserva'}


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'cabana_apps/confirm_delete.html'
    success_url = '/abm/reservas/'


class AlquilerListView(ListView):
    model = Alquiler
    template_name = 'cabana_apps/list.html'
    context_object_name = 'objetos'
    extra_context = {'titulo': 'Alquileres', 'crear_url': 'alquiler_create', 'editar_url': 'alquiler_update', 'borrar_url': 'alquiler_delete'}


class AlquilerCreateView(CreateView):
    model = Alquiler
    form_class = AlquilerForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Nuevo alquiler'}


class AlquilerUpdateView(UpdateView):
    model = Alquiler
    form_class = AlquilerForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Editar alquiler'}


class AlquilerDeleteView(DeleteView):
    model = Alquiler
    template_name = 'cabana_apps/confirm_delete.html'
    success_url = '/abm/alquileres/'


class PagoListView(ListView):
    model = Pago
    template_name = 'cabana_apps/list.html'
    context_object_name = 'objetos'
    extra_context = {'titulo': 'Pagos', 'crear_url': 'pago_create', 'editar_url': 'pago_update', 'borrar_url': 'pago_delete'}


class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Nuevo pago'}


class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Editar pago'}


class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'cabana_apps/confirm_delete.html'
    success_url = '/abm/pagos/'


class RegistroListView(ListView):
    model = Registro
    template_name = 'cabana_apps/list.html'
    context_object_name = 'objetos'
    extra_context = {'titulo': 'Registros', 'crear_url': 'registro_create', 'editar_url': 'registro_update', 'borrar_url': 'registro_delete'}


class RegistroCreateView(CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Nuevo registro'}


class RegistroUpdateView(UpdateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'cabana_apps/form.html'
    extra_context = {'titulo': 'Editar registro'}


class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = 'cabana_apps/confirm_delete.html'
    success_url = '/abm/registros/'
