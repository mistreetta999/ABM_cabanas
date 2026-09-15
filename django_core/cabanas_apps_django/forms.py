from django import forms
from .models import Cliente, Pago, Registro, Reserva, Alquiler


class CabanaForm(forms.ModelForm):
    class Meta:
        model = Cabana
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = "__all__"


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = "__all__"


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"


class AlquierForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = "__all__"


class ChatbotForm(forms.ModelForm):
    class Meta:
        model = Chatbot
        fields = "__all__"


class WebForm(forms.ModelForm):
    class Meta:
        model = Web
        fields = "__all__"


class TemplatesForm(forms.ModelForm):
    class Meta:
        model = Templates
        fields = "__all__"
