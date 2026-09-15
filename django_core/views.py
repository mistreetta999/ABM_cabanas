from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Importa tus modelos reales de tus apps
from django_core.cabanas_apps_django.cabanas.models import Cabana
from django_core.cabanas_apps_django.clientes.models import Cliente
from django_core.cabanas_apps_django.reservas.models import Reserva
from django_core.cabanas_apps_django.pagos.models import Pago

@login_required
def dashboard_interactivo(request):
    context = {
        'cabanas': Cabana.objects.all(),
        'clientes': Cliente.objects.all().order_by('-id')[:5], # Últimos 5
        'reservas': Reserva.objects.all().order_by('-fecha_inicio'),
        'pagos': Pago.objects.all().order_by('-id')[:5],
        # Contadores rápidos para las tarjetas interactivas
        'total_cabanas': Cabana.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'total_reservas': Reserva.objects.count(),
    }
    return render(request, 'dashboard/interactivo.html', context)
