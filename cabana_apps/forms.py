from django import forms

from .models import Alquiler, Cabana, Cliente, Pago, Registro, Reserva


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = 'form-check-input'
            field.widget.attrs.setdefault('class', css_class)


class ClienteForm(BootstrapModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'telefono', 'email']


class CabanaForm(BootstrapModelForm):
    class Meta:
        model = Cabana
        fields = ['nombre', 'capacidad', 'precio_por_noche', 'disponible']


class ReservaForm(BootstrapModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'cabana', 'fecha_ingreso', 'fecha_salida', 'estado', 'observaciones']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }


class AlquilerForm(BootstrapModelForm):
    class Meta:
        model = Alquiler
        fields = ['reserva', 'cliente', 'cabana', 'fecha_inicio', 'fecha_fin', 'monto_total', 'estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class PagoForm(BootstrapModelForm):
    class Meta:
        model = Pago
        fields = ['alquiler', 'fecha', 'monto', 'metodo', 'comprobante']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class RegistroForm(BootstrapModelForm):
    class Meta:
        model = Registro
        fields = ['modulo', 'descripcion', 'responsable']
