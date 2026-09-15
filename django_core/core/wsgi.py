import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_core.core.settings')
application = get_wsgi_application() Haus = os.environ.get('RUN_MAIN')
if Haus == 'true': os.system('start http://localhost:8000/')
