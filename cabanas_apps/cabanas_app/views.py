from django.shortcuts import render, get_object_or_404, redirect
from .models import Cabana
from .forms import CabanaForm

""" Vistas CRUD para el modelo Cabana """

# Listar todas las cabañas
def cabana_list(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas_app/cabana_list.html", {"cabanas": cabanas})

# Ver detalle de una cabaña
def cabana_detail(request, pk):
    cabana = get_object_or_404(Cabana, pk=pk)
    return render(request, "cabanas_app/cabana_detail.html", {"cabana": cabana})

# Crear nueva cabaña
def cabana_create(request):
    if request.method == "POST":
        form = CabanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cabanas_app:cabana_list")
    else:
        form = CabanaForm()
    return render(request, "cabanas_app/cabana_form.html", {"form": form})

# Editar cabaña existente
def cabana_update(request, pk):
