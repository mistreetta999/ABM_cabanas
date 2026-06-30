"""Este archivo contiene las vistas de la app registros."""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Cliente, Reserva, Alquiler, Pago, Registro
from .forms import ClienteForm, ReservaForm, AlquilerForm, PagoForm, RegistroForm

# Panel principal
def panel_django(request):
    return render(request, "panel_django.html")

# --- CLIENTES ---
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/list.html", {"clientes": clientes})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm()
    return render(request, "clientes/form.html", {"form": form})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "clientes/form.html", {"form": form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect("cliente_list")

# --- RESERVAS ---
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, "reservas/list.html", {"reservas": reservas})

def reserva_create(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reserva_list")
    else:
        form = ReservaForm()
    return render(request, "reservas/form.html", {"form": form})

# (similar para editar y borrar reservas)

# --- ALQUILERES ---
def alquiler_list(request):
    alquileres = Alquiler.objects.all()
    return render(request, "alquileres/list.html", {"alquileres": alquileres})

def alquiler_create(request):
    if request.method == "POST":
        form = AlquilerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alquiler_list")
    else:
        form = AlquilerForm()
    return render(request, "alquileres/form.html", {"form": form})

# --- PAGOS ---
def pago_list(request):
    pagos = Pago.objects.all()
    return render(request, "pagos/list.html", {"pagos": pagos})

def pago_create(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pago_list")
    else:
        form = PagoForm()
    return render(request, "pagos/form.html", {"form": form})

# --- REGISTROS ---
def registro_list(request):
    registros = Registro.objects.all()
    return render(request, "registros/list.html", {"registros": registros})

def registro_create(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro_list")
    else:
        form = RegistroForm()
    return render(request, "registros/form.html", {"form": form})
