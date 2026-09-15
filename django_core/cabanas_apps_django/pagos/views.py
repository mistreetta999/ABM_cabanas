"""Vistas para la gestión de pagos."""

from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Pago


class PagoListView(View):
    """Lista todos los pagos registrados"""

    def get(self, request):
        """Obtiene y muestra la lista de todos los pagos registrados."""
        pagos = Pago.objects.all()  # pylint: disable=no-member
        return render(request, "pagos/lista_pagos.html", {"pagos": pagos})


class PagoDetailView(View):
    """Muestra el detalle de un pago específico"""

    def get(self, request, pk):
        """Obtiene y muestra el detalle de un pago específico."""
        pago = get_object_or_404(Pago, pk=pk)
        return render(request, "pagos/detalle_pago.html", {"pago": pago})


class PagoCreateView(View):
    """Formulario para crear un nuevo pago"""

    def get(self, request):
        """Muestra el formulario para crear un nuevo pago."""
        return render(request, "pagos/crear_pago.html")

    def post(self, request):
        """Procesa el formulario y crea un nuevo pago."""
        # lógica para guardar el pago
        # ejemplo mínimo: solo mostrar confirmación
        return render(
            request, "pagos/crear_pago.html", {"mensaje": "Pago creado correctamente"}
        )


class PagoUpdateView(View):
    """Formulario para editar un pago existente"""

    def get(self, request, pk):
        """Muestra el formulario para editar un pago existente."""
        pago = get_object_or_404(Pago, pk=pk)
        return render(request, "pagos/editar_pago.html", {"pago": pago})

    def post(self, request, pk):
        """Procesa el formulario y actualiza un pago existente."""
        # lógica para actualizar el pago
        pago = get_object_or_404(Pago, pk=pk)
        return render(
            request,
            "pagos/editar_pago.html",
            {"pago": pago, "mensaje": "Pago actualizado correctamente"},
        )


class PagoDeleteView(View):
    """Confirma y elimina un pago"""

    def get(self, request, pk):
        """Muestra la confirmación para eliminar un pago."""
        pago = get_object_or_404(Pago, pk=pk)
        return render(request, "pagos/eliminar_pago.html", {"pago": pago})

    def post(self, request, pk):
        """Elimina un pago específico."""
        pago = get_object_or_404(Pago, pk=pk)
        pago.delete()
        return render(
            request,
            "pagos/eliminar_pago.html",
            {"mensaje": "Pago eliminado correctamente"},
        )
