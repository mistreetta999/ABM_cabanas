# django_core/handlers.py
from django.conf import settings
from django.http import JsonResponse, HttpResponse

# Estado general del sistema
def sistema_status(request):
    return HttpResponse("✅ Sistema de gestión de cabañas activo y corriendo")

# Configuración básica
def mostrar_settings(request):
    data = {
        "DEBUG": settings.DEBUG,
        "LANGUAGE_CODE": settings.LANGUAGE_CODE,
        "TIME_ZONE": settings.TIME_ZONE,
        "DATABASES": settings.DATABASES,
    }
    return JsonResponse(data, safe=False)

# Apps instaladas
def listar_apps(request):
    return JsonResponse({"INSTALLED_APPS": settings.INSTALLED_APPS}, safe=False)

# Middleware configurado
def listar_middleware(request):
    return JsonResponse({"MIDDLEWARE": settings.MIDDLEWARE}, safe=False)

# Configuración de base de datos
def db_config(request):
    return JsonResponse(settings.DATABASES, safe=False)

# Configuración de rutas estáticas
def static_config(request):
    data = {
        "STATIC_URL": settings.STATIC_URL,
        "STATICFILES_DIRS": getattr(settings, "STATICFILES_DIRS", []),
    }
    return JsonResponse(data, safe=False)

# Configuración de media
def media_config(request):
    data = {
        "MEDIA_URL": settings.MEDIA_URL,
        "MEDIA_ROOT": settings.MEDIA_ROOT,
    }
    return JsonResponse(data, safe=False)
