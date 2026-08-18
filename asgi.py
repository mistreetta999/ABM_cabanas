"""ASGI config for cabanas project."""

import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabanas_principal.settings.settings')

application = get_asgi_application()
