# Sistema de gestion de cabanas

Proyecto Django para administrar cabanas, clientes, reservas y un chatbot simple de consultas.

## Estructura principal

- `manage.py`: entrada estandar de Django.
- `main.py`: entrada alternativa que inicializa Django y levanta el servidor local si no se pasa otro comando.
- `cabanas_project/`: configuracion principal del proyecto.
- `cabana_apps/`: app de gestion de clientes, cabanas y reservas.
- `chatbot/`: app del chatbot.
- `Template/`: plantillas HTML usadas por Django.
- `static/`: archivos estaticos servidos por Django.
- `DATABASE/`, `django_core/`, `django_local/`: material restaurado del proyecto original.

## Uso local

```powershell
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

Tambien se puede usar:

```powershell
.venv\Scripts\python.exe main.py
```

En Windows, el archivo `levantar_programa.bat` ejecuta las migraciones y levanta el servidor local.

## Rutas utiles

- `/`: pagina principal.
- `/cabanas/`: panel Django.
- `/panel-html/`: panel HTML separado.
- `/abm/clientes/`: gestion de clientes.
- `/abm/cabanas/`: gestion de cabanas.
- `/abm/reservas/`: gestion de reservas.
- `/chatbot/`: chatbot.
- `/admin/`: administracion Django.

