from django import forms
from django import forms
from .models import Alquiler

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ["cabana", "cliente", "reserva", "monto_total", "fecha_pago"]

        labels = {
            "cabana": "Cabaña",
            "cliente": "Cliente",
            "reserva": "Reserva",
            "monto_total": "Monto total",
            "fecha_pago": "Fecha de pago",
        }

        widgets = {
            "cabana": forms.Select(attrs={"class": "form-control"}),
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "reserva": forms.Select(attrs={"class": "form-control"}),
            "monto_total": forms.NumberInput(attrs={"class": "form-control"}),
            "fecha_pago": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
