from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    """Formulario para crear y editar reservas"""

    class Meta:
        model = Reserva
        fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "estado"]

        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "cliente": forms.Select(attrs={"class": "form-select"}),
            "cabana": forms.Select(attrs={"class": "form-select"}),
        }

        labels = {
            "cliente": "Cliente",
            "cabana": "Cabaña",
            "fecha_inicio": "Fecha de inicio",
            "fecha_fin": "Fecha de fin",
            "estado": "Estado de la reserva",
        }
