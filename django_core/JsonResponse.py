from django.http import JsonResponse

def cabana_list_json(request):
    data = {
        "cabanas": [
            {"nombre": "Cabaña Verde", "capacidad": 4, "precio_base": 1200},
            {"nombre": "Cabaña Azul", "capacidad": 6, "precio_base": 1800},
        ]
    }
    return JsonResponse(data)
