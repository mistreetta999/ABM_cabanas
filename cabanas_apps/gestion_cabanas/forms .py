""""Forms for the cabanas_apps application.
"""
from django import forms

from .models import Alquiler, Cabana, Cliente, Pago, Registro, Reserva


class BootstrapModelForm(forms.ModelForm):
    """A base form class that adds Bootstrap classes to form fields.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = 'form-check-input'
            field.widget.attrs.setdefault('class', css_class)


class ClienteForm(BootstrapModelForm):
    """Form para el modelo Cliente."""
    class Meta:
        """"Meta class para ClienteForm."""
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'telefono', 'email']


class CabanaForm(BootstrapModelForm):
    """Form para el modelo Cabana."""
    class Meta:
        """"Meta class para CabanaForm."""
        model = Cabana
        fields = ['nombre', 'capacidad', 'precio_por_noche', 'disponible']


class ReservaForm(BootstrapModelForm):
    """Form para el modelo Reserva."""
    class Meta:
        """"Meta class para ReservaForm."""
        model = Reserva
        fields = ['cliente', 'cabana', 'fecha_ingreso', 'fecha_salida', 'estado', 'observaciones']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }


class AlquilerForm(BootstrapModelForm):
    """Form para el modelo Alquiler."""
    class Meta:
        """"Meta class para AlquilerForm."""
        model = Alquiler
        fields:list = ['reserva', 'cliente', 'cabana', 'fecha_inicio', 'fecha_fin', 'monto_total', 'estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class PagoForm(BootstrapModelForm):
    """Form para el modelo Pago."""
    class Meta:
        """"Meta class para PagoForm."""
        model = Pago
        fields = ['alquiler', 'fecha', 'monto', 'metodo', 'comprobante']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class RegistroForm(BootstrapModelForm):
    """Form para el modelo Registro."""
    class Meta:
        """"Meta class para RegistroForm."""
        model = Registro
        fields = ['modulo', 'descripcion', 'responsable']
