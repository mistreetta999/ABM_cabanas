from django.shortcuts import get_object_or_404, render

from .models import Publicacion


def lista(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "pagina_principal.html", {"publicaciones": publicaciones})


def detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, "pagina_principal.html", {"publicacion": publicacion})
