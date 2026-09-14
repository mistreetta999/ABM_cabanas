from rest_framework import serializers
from django_core.cabanas_apps_django.reservas.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
