"""Handlers auxiliares de AppConfig."""
from django.http import JsonResponse


def estado_appconfig(request):
    """Devuelve un estado simple de AppConfig."""
    del request
    return JsonResponse({"appconfig": "OK"})
