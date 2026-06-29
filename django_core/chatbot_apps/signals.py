from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from cabanas_apps.chatbot_app.chatbot.models import Chatbot


@receiver(post_save, sender=Chatbot)
def chatbot_post_save(sender, instance, created, **kwargs):
    """Maneja el evento de guardado de un chatbot."""
    accion = "creado" if created else "actualizado"
    print(f"Chatbot '{instance.nombre}' {accion} exitosamente.")


@receiver(post_delete, sender=Chatbot)
def chatbot_post_delete(sender, instance, **kwargs):
    """Maneja el evento de eliminación de un chatbot."""
    print(f"Chatbot '{instance.nombre}' eliminado exitosamente.")
