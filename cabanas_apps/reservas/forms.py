""" archivo de formularios para la app de reservas """
from django.shortcuts import render, redirect
from .forms import Reservas

def crear_reserva(request):
    if request.method == 'POST':
        form = Reservas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = Reservas()
    return render(request, 'reservas/crear.html', {'form': form})
