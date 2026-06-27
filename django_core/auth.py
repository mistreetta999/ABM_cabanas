from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    """
    Permite autenticación usando email o username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Buscar por email o username
            user = User.objects.filter(email=username).first() or User.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None
