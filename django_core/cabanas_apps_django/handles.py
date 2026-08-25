"""Manejadores de vistas para cabanas_apps_django"""

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django_core.cabanas_apps_django.models import Cabanas

def listar(request, modelo, template_name):
    """Lista objetos de un modelo dado"""
    objetos = modelo.objects.all()
    return render(request, template_name, {"objetos": objetos})


def crear(request, models, form_class, template_name, redirect_url):
    """Crea un objeto de un modelo dado"""
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, template_name, {"form": form})


def editar(request, modelo, form_class, pk, template_name, redirect_url):
    """Edita un objeto existente"""
    objeto = get_object_or_404(modelo, pk=pk)
    if request.method == "POST":
        form = form_class(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=objeto)
    return render(request, template_name, {"form": form, "objeto": objeto})


def borrar(request, modelo, pk, redirect_url):
    """Elimina un objeto existente"""
    objeto = get_object_or_404(modelo, pk=pk)
    objeto.delete()
    return redirect(redirect_url)


def ver(request, modelo, pk, template_name):
    """Muestra detalle de un objeto"""
    objeto = get_object_or_404(modelo, pk=pk)
    return render(request, template_name, {"objeto": objeto})


def listar_cabanas(request):
    """lista"""
    return listar(request, Cabana, "cabanas/lista.html")

def crear_cabana(request, form_class):
    """ crear"""
    return crear(request, Cabana, form_class, "cabanas/formulario.html", reverse("cabana_list"))

def editar_cabana(request, form_class, pk):
    """ editar"""
    return editar(request, Cabana, form_class, pk, "cabanas/formulario.html", reverse("cabana_list"))

def borrar_cabana(request, pk):
    """ borrar"""
    return borrar(request, Cabana, pk, reverse("cabana_list"))

def ver_cabana(request, pk):
          """ ver cabanas"""
    return ver(request, Cabana, pk, "cabanas/detalle.html")
