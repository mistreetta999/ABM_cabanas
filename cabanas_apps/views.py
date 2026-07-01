from django.shortcuts import renderSTATIC_URL = "/static/"
from .models import Cliente, Cabana, Reserva, Alquiler, RegistroSTATIC_URL = "/static/"
from django.urls import reverse_lazySTATIC_URL = "/static/"
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteViewSTATIC_URL = "/static/"
""" Vistas de la aplicación Cabañas."""STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


def pagina_principal(request): STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

return render(request, "pagina_principal.html")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# Vista de inicioSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class InicioView(TemplateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para la página de inicio """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "inicio.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# Panel genéricoSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class PanelView(TemplateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para el panel genérico """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "panel.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# ClientesSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ClienteListView(ListView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para listar los clientes """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ClienteSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "clientes/list.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ClienteCreateView(CreateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para crear un nuevo cliente """   STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ClienteSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["nombre", "email", "telefono"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "clientes/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("cliente_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ClienteUpdateView(UpdateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para actualizar un cliente existente """  STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ClienteSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["nombre", "email", "telefono"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "clientes/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("cliente_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ClienteDeleteView(DeleteView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para eliminar un cliente existente """  STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ClienteSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "clientes/confirm_delete.html"  STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("cliente_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# CabanasSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class CabanaListView(ListView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para listar las cabañas """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = CabanaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "cabanas/list.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class CabanaCreateView(CreateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para crear una nueva cabaña """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = CabanaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "cabanas/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("cabana_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class CabanaUpdateView(UpdateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para actualizar una cabaña existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = CabanaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["nombre", "capacidad", "precio_por_noche", "precio_por_cabana"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "cabanas/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("cabana_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class CabanaDeleteView(DeleteView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para eliminar una cabaña existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = CabanaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "cabanas/confirm_delete.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("cabana_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# ReservasSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ReservaListView(ListView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para listar las reservas """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ReservaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "reservas/list.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ReservaCreateView(CreateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ReservaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "estado"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "reservas/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("reserva_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ReservaUpdateView(UpdateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para actualizar una reserva existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ReservaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "estado"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "reservas/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("reserva_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class ReservaDeleteView(DeleteView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = ReservaSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "reservas/confirm_delete.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("reserva_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# AlquileresSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class AlquilerListView(ListView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para listar los alquileres """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = AlquilerSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "alquileres/list.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class AlquilerCreateView(CreateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para crear un nuevo alquiler """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = AlquilerSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "alquileres/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("alquiler_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class AlquilerUpdateView(UpdateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para actualizar un alquiler existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = AlquilerSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "alquileres/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("alquiler_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class AlquilerDeleteView(DeleteView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para eliminar un alquiler existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = AlquilerSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "alquileres/confirm_delete.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("alquiler_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# RegistrosSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class RegistroListView(ListView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para listar los registros """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = RegistroSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "registros/list.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class RegistroCreateView(CreateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para crear un nuevo registro """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = RegistroSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["reserva", "cliente", "detalle"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "registros/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("registro_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class RegistroUpdateView(UpdateView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para actualizar un registro existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = RegistroSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

fields = ["reserva", "cliente", "detalle"]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "registros/form.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("registro_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'


class RegistroDeleteView(DeleteView):
    STATIC_URL = "/static/"


STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

""" Vista para eliminar un registro existente """STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

model = RegistroSTATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

template_name = "registros/confirm_delete.html"STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

success_url = reverse_lazy("registro_list")STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'
