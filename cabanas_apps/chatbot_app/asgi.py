""" archivo asgi de la app chatbot_app
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabanas.settings')

application = get_asgi_application()
