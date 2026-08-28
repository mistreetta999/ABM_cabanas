"""
Vistas de la aplicación Usuarios.
Permite gestionar usuarios del sistema.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class UsuarioListView(ListView):
    """Lista todos los usuarios registrados."""
    model = User
    template_name = "usuarios/usuario_list.html"
    context_object_name = "usuarios"
    paginate_by = 20


class UsuarioDetailView(DetailView):
    """Muestra el detalle de un usuario específico."""
    model = User
    template_name = "usuarios/usuario_detail.html"
    context_object_name = "usuario"


class UsuarioCreateView(CreateView):
    """Permite registrar un nuevo usuario."""
    model = User
    template_name = "usuarios/usuario_form.html"
    fields = ["username", "first_name", "last_name", "email", "password"]
    success_url = reverse_lazy("usuarios:usuario_list")

    def form_valid(self, form):
        # Guardar el usuario con contraseña encriptada
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)


class UsuarioUpdateView(UpdateView):
    """Permite editar un usuario existente."""
    model = User
    template_name = "usuarios/usuario_form.html"
    fields = ["username", "first_name", "last_name", "email"]
    success_url = reverse_lazy("usuarios:usuario_list")


class UsuarioDeleteView(DeleteView):
    """Permite eliminar un usuario."""
    model = User
    template_name = "usuarios/usuario_confirm_delete.html"
    success_url = reverse_lazy("usuarios:usuario_list")
