""" handles para busascar las aplicaciones de django """
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Reserva, Alquiler, Pago, Registro
from .forms import ClienteForm, ReservaForm, AlquilerForm, PagoForm, RegistroForm


# Panel principal
def panel_django(request):
    """ Muestra el panel principal de la aplicación Django. """
    return render(request, "panel_django.html")

# --- CLIENTES ---


def cliente_list(request):
    """ Muestra la lista de clientes registrados en la aplicación Django. """
    clientes = Cliente.objects.all()
    return render(request, "clientes/list.html", {"clientes": clientes})


def cliente_create(request):
    """ Permite crear un nuevo cliente en la aplicación Django. """
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cliente_list")
    return render(request, "clientes/form.html", {"form": form})


def cliente_edit(request, pk):
    """ Permite editar un cliente existente en la aplicación Django. """
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("cliente_list")
    return render(request, "clientes/form.html", {"form": form})


def cliente_delete(request, pk):
    """ Permite borrar un cliente existente en la aplicación Django. """
    _ = request
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect("cliente_list")

# --- RESERVAS ---


def reserva_list(request):
    """ Muestra la lista de reservas registradas en la aplicación Django. """
    reservas = Reserva.objects.all()
    return render(request, "reservas/list.html", {"reservas": reservas})


def reserva_create(request):
    """ Permite crear una nueva reserva en la aplicación Django. """
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("reserva_list")
    return render(request, "reservas/form.html", {"form": form})

# (similar para editar y borrar reservas)

# --- ALQUILERES ---


def alquiler_list(request):
    """ Muestra la lista de alquileres registrados en la aplicación Django. """
    alquileres = Alquiler.objects.all()
    return render(request, "alquileres/list.html", {"alquileres": alquileres})


def alquiler_create(request):
    """ Permite crear un nuevo alquiler en la aplicación Django. """
    form = AlquilerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("alquiler_list")
    return render(request, "alquileres/form.html", {"form": form})

# --- PAGOS ---


def pago_list(request):
    """ Muestra la lista de pagos registrados en la aplicación Django. """
    pagos = Pago.objects.all()
    return render(request, "pagos/list.html", {"pagos": pagos})


def pago_create(request):
    """ Permite crear un nuevo pago en la aplicación Django. """
    form = PagoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("pago_list")
    return render(request, "pagos/form.html", {"form": form})

# --- REGISTROS ---


def registro_list(request):
    """ Muestra la lista de registros registrados en la aplicación Django. """
    registros = Registro.objects.all()
    return render(request, "registros/list.html", {"registros": registros})


def registro_create(request):
    """ Permite crear un nuevo registro en la aplicación Django. """
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("registro_list")
    return render(request, "registros/form.html", {"form": form})
