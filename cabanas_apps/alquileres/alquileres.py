from django.shortcuts import render, get_object_or_404, redirect
from cabanas_apps.gestion_cabanas.models import Alquiler, Cliente, Cabana, Reserva

def listar_alquileres(request):
    """Muestra todos los alquileres."""
    alquileres = Alquiler.objects.all()
    return render(request, "pagina_principal/lista.html", {"alquileres": alquileres})

def detalle_alquiler(request, alquiler_id):
    """Muestra el detalle de un alquiler específico."""
    alquiler = get_object_or_404(Alquiler, pk=alquiler_id)
    return render(request, "pagina_principal/detalle.html", {"alquiler": alquiler})

def crear_alquiler(request, reserva_id):
    """Crea un nuevo alquiler a partir de una reserva."""
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    cliente = reserva.cliente
    cabana = reserva.cabana

    if request.method == "POST":
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        monto_total = request.POST.get("monto_total", 0)

        alquiler = Alquiler.objects.create(
            reserva=reserva,
            cliente=cliente,
            cabana=cabana,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            monto_total=monto_total,
            estado="activo"
        )
        return redirect("detalle_alquiler", alquiler_id=alquiler.id)

    return render(request, "pagina_principal/formulario.html", {"reserva": reserva})

def borrar_alquiler(request, alquiler_id):
    """Elimina un alquiler existente."""
    alquiler = get_object_or_404(Alquiler, pk=alquiler_id)

    if request.method == "POST":
        alquiler.delete()
        return redirect("listar_alquileres")

    return render(request, "pagina_principal/confirma_borrar.html", {"alquiler": alquiler})
