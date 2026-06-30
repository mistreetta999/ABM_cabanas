""" views genrales para la aplicación de gestión de cabanas """
from django.shortcuts import render
from django.http import HttpResponse

# Panel principal
def panel_django(request):
    return render(request, "panel_django.html")

# Clientes
def cliente_list(request):
    return HttpResponse("Listado de clientes")
def cliente_create(request):
    return HttpResponse("Crear cliente")

# Reservas
def reserva_list(request):
    return HttpResponse("Listado de reservas")
def reserva_create(request):
    return HttpResponse("Crear reserva")

# Alquileres
def alquiler_list(request):
    return HttpResponse("Listado de alquileres")
def alquiler_create(request):
    return HttpResponse("Crear alquiler")

# Pagos
def pago_list(request):
    return HttpResponse("Listado de pagos")
def pago_create(request):
    return HttpResponse("Registrar pago")

# Registros
def registro_list(request):
    return HttpResponse("Listado de registros")
def registro_create(request):
    return HttpResponse("Crear registro")
