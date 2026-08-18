""" archivo pagos para pagar"""
from django.shortcuts import render, get_object_or_404, redirect
from cabanas_apps.pagos.models import Pago
from cabanas_apps.alquileres.models import Alquiler
from cabanas_apps.clientes.models import Cliente
from django.urls import reverse



class Pagos:
    """Clase que maneja los pagos de un alquiler."""
    def __init__(self, alquiler_id):
        self.alquiler_id = alquiler_id
        self.reserva_id = alquiler_id
    def pagos (self):
        """Obtiene todos los pagos asociados a un alquiler específico."""
        pagos = Pago.objects.filter(alquiler_id=self.alquiler_id)
        return pagos

def listar_pagos(request):
    """Muestra todos los pagos registrados."""
    pagos = Pago.objects.all()
    return render(request, "pagos/panel.html", {"pagos": pagos})

def detalle_pago(request, pago_id):
    """Muestra el detalle de un pago específico."""
    pago = get_object_or_404(Pago, pk=pago_id)
    return render(request, "pagos/panel.html", {"pago": pago})

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

    return render(request, "pagos/panel.html", {"alquiler": alquiler})

def borrar_pago(request, pago_id):
    """Elimina un pago existente."""
    pago = get_object_or_404(Pago, pk=pago_id)

    if request.method == "POST":
        pago.delete()
        return redirect("listar_pagos")

    return render(request, "pagos/panel.html", {"pago": pago})
def boton (self)->Any:
    """Genera botones de acción para la Cabanas
 en el admin."""
    editar = reverse('admin:cabanas_cabana_change', args=[self.pk])
    eliminar = reverse('admin:cabanas_cabana_delete', args=[self.pk])
    crear = reverse('admin:cabanas_cabana_add')
    imprimir = reverse('admin:cabanas_cabana_print', args=[self.pk])
    buscar = reverse('admin:cabanas_cabana_changelist')
    salir = reverse('admin:index')
    return boton
