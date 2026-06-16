from django.apps import AppConfig

class RegistrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabana_apps.registros'
# cabanas_app/reservas/apps.py
class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_app.reservas' # <--- DEBE COINCIDIR CON SETTINGS

# cabanas_app/usuarios/apps.py
class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_app.usuarios' # <--- DEBE COINCIDIR CON    
     # SETTINGS
    verbose_name = 'Usuarios' # <--- NOMBRE EN EL A DASHBOARD DE DJANGO
    # DEBE COINCID  IR CON SETTINGS
    label = 'registros' 