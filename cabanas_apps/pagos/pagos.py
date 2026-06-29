from django.shortcuts import render, get_object_or_404, redirect
from cabanas_apps.gestion_cabanas.models import Pago, Alquiler

def listar_pagos(request):
    """Muestra todos los pagos registrados."""
    pagos = Pago.objects.all()
    return render(request, "pagina_principal/lista.html", {"pagos": pagos})

def detalle_pago(request, pago_id):
    """Muestra el detalle de un pago específico."""
    pago = get_object_or_404(Pago, pk=pago_id)
    return render(request, "pagina_principal/detalle.html", {"pago": pago})

def crear_pago(request, alquiler_id):
    """Crea un nuevo pago asociado a un alquiler."""
    alquiler = get_object_or_404(Alquiler, pk=alquiler_id)

    if request.method == "POST":
        fecha = request.POST.get("fecha")
        monto = request.POST.get("monto")
        metodo = request.POST.get("metodo")
        comprobante = request.POST.get("comprobante", "")

        pago = Pago.objects.create(
            alquiler=alquiler,
            fecha=fecha,
            monto=monto,
            metodo=metodo,
            comprobante=comprobante
        )
        return redirect("detalle_pago", pago_id=pago.id)

    return render(request, "pagina_principal/formulario.html", {"alquiler": alquiler})

def borrar_pago(request, pago_id):
    """Elimina un pago existente."""
    pago = get_object_or_404(Pago, pk=pago_id)

    if request.method == "POST":
        pago.delete()
        return redirect("listar_pagos")

    return render(request, "pagina_principal/confirma_borrar.html", {"pago": pago})
