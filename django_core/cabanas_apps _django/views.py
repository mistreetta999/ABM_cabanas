"""interfaz_gestion_cabanas con botones Python para django_core/cabanas_apps _django."""
from html import escape

from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404, redirect
from django.db import OperationalError, ProgrammingError

from cabanas_apps.alquileres.models import Alquiler
from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.chatbot_app.models import Chatbot
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.pagos.models import Pago
from cabanas_apps.registros.models import Registro
from cabanas_apps.reservas.models import Reserva

# cabanas_apps/interfaz_gestion_cabanas/views.py
from django.http import JsonResponse
# cabanas_apps/interfaz_gestion_cabanas/views.py
from django.http import JsonResponse

def Cabanas
(request):
    return JsonResponse({"vista": "Cabanas
 funcionando"})

def Alquileres(request):
    return JsonResponse({"vista": "Alquileres funcionando"})

def Usuarios(request):
    return JsonResponse({"vista": "Usuarios funcionando"})

def Reservas(request):
    return JsonResponse({"vista": "Reservas funcionando"})

def Pagos(request):
    return JsonResponse({"vista": "Pagos funcionando"})

def Registros(request):
    return JsonResponse({"vista": "Registros funcionando"})

def Chatbot(request):
    return JsonResponse({"vista": "Chatbot funcionando"})

def Clientes(request):
    return JsonResponse({"vista": "Clientes funcionando"})

def Cabanas
(request):
    return JsonResponse({"mensaje": "Vista Cabanas
 funcionando"})

def Alquileres(request):
    return JsonResponse({"mensaje": "Vista Alquileres funcionando"})

def Usuarios(request):
    return JsonResponse({"mensaje": "Vista Usuarios funcionando"})

def Reservas(request):
    return JsonResponse({"mensaje": "Vista Reservas funcionando"})

def Pagos(request):
    return JsonResponse({"mensaje": "Vista Pagos funcionando"})

def Registros(request):
    return JsonResponse({"mensaje": "Vista Registros funcionando"})

def Chatbot(request):
    return JsonResponse({"mensaje": "Vista Chatbot funcionando"})

def Clientes(request):
    return JsonResponse({"mensaje": "Vista Clientes funcionando"})

BASE_URL = "/django_core/cabanas_apps_django"

CRUD_APPS = {
    "cabanas": {
        "titulo": "Cabanas",
        "modelo": Cabanas
,
        "campos": ["nombre", "capacidad", "precio_por_noche", "disponible"],
    },
    "clientes": {
        "titulo": "Clientes",
        "modelo": Cliente,
        "campos": ["dni", "nombre", "apellido", "direccion", "telefono"],
    },
    "reservas": {
        "titulo": "Reservas",
        "modelo": Reserva,
        "campos": ["cliente", "Cabanas
", "fecha_inicio", "fecha_fin", "estado"],
    },
    "alquileres": {
        "titulo": "Alquileres",
        "modelo": Alquiler,
        "campos": ["cabanas", "cliente", "reservas", "monto_total", "fecha_pago"],
    },
    "pagos": {
        "titulo": "Pagos",
        "modelo": Pago,
        "campos": ["alquiler", "fecha", "monto", "metodo", "comprobante"],
    },
    "registros": {
        "titulo": "Registros",
        "modelo": Registro,
        "campos": ["usuario", "accion", "descripcion", "monto"],
    },
    "chatbot": {
        "titulo": "Chatbot",
        "modelo": Chatbot,
        "campos": ["nombre", "descripcion"],
    },
}


def render_python(titulo: str, contenido: str) -> HttpResponse:
    """Render HTML desde Python, sin archivos ni motor de templates."""
    safe_title = escape(titulo)
    nav_links = "".join(
        f'<a href="{BASE_URL}/{escape(slug)}/">{escape(config["titulo"])}</a>'
        for slug, config in CRUD_APPS.items()
    )
    html = f"""<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{safe_title}</title>
    <style>
        :root {{
            --ink: #16201d;
            --muted: #60706a;
            --line: #dce5e0;
            --panel: #ffffff;
            --wash: #eef5f1;
            --green: #24734e;
            --green-dark: #165137;
            --teal: #0f6f78;
            --gold: #af7a18;
            --red: #a33b3b;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: var(--wash);
            color: var(--ink);
        }}
        .shell {{
            min-height: 100vh;
            display: grid;
            grid-template-columns: 250px minmax(0, 1fr);
        }}
        aside {{
            background: #18241f;
            color: #f7fbf8;
            padding: 22px 18px;
        }}
        .brand {{
            display: block;
            color: #ffffff;
            text-decoration: none;
            font-size: 20px;
            font-weight: 800;
            margin-bottom: 6px;
        }}
        .subtitle {{
            color: #b9c9c1;
            font-size: 13px;
            line-height: 1.4;
            margin: 0 0 22px;
        }}
        nav {{
            display: grid;
            gap: 6px;
        }}
        nav a {{
            color: #e8f2ed;
            text-decoration: none;
            padding: 10px 11px;
            border-radius: 6px;
            font-size: 14px;
        }}
        nav a:hover {{
            background: rgba(255, 255, 255, 0.1);
        }}
        main {{
            width: 100%;
            max-width: 1180px;
            padding: 28px;
        }}
        .topbar {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 18px;
            margin-bottom: 22px;
        }}
        h1 {{
            margin: 0;
            font-size: 30px;
            line-height: 1.15;
        }}
        h2 {{
            margin: 0 0 14px;
            font-size: 22px;
        }}
        .eyebrow {{
            color: var(--teal);
            font-size: 12px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0;
            margin-bottom: 6px;
        }}
        .lead {{
            color: var(--muted);
            margin: 8px 0 0;
            line-height: 1.5;
        }}
        .toolbar {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
            margin: 16px 0;
        }}
        .button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 38px;
            padding: 9px 13px;
            border-radius: 6px;
            border: 1px solid var(--line);
            color: var(--ink);
            background: var(--panel);
            text-decoration: none;
            font-weight: 700;
            cursor: pointer;
        }}
        .button.primary {{
            border-color: var(--green);
            background: var(--green);
            color: white;
        }}
        .button.danger {{
            border-color: #e1bbbb;
            color: var(--red);
        }}
        .button.danger.primary {{
            background: var(--red);
            border-color: var(--red);
            color: white;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 12px;
        }}
        .module {{
            display: block;
            min-height: 128px;
            padding: 18px;
            border-radius: 8px;
            background: var(--panel);
            border: 1px solid var(--line);
            text-decoration: none;
            color: var(--ink);
        }}
        .module:hover {{
            border-color: var(--green);
            box-shadow: 0 12px 26px rgba(17, 38, 29, 0.09);
        }}
        .module strong {{
            display: block;
            font-size: 18px;
            margin-bottom: 8px;
        }}
        .module span {{
            color: var(--muted);
            font-size: 13px;
            line-height: 1.45;
        }}
        .statbar {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 10px;
            margin: 0 0 18px;
        }}
        .stat {{
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 14px;
        }}
        .stat b {{
            display: block;
            font-size: 24px;
        }}
        .stat span {{
            color: var(--muted);
            font-size: 13px;
        }}
        .table-wrap {{
            overflow-x: auto;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--panel);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            min-width: 720px;
        }}
        th, td {{
            padding: 13px 14px;
            border-bottom: 1px solid var(--line);
            text-align: left;
            vertical-align: top;
        }}
        th {{
            background: #f8fbf9;
            color: var(--muted);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0;
        }}
        tr:last-child td {{
            border-bottom: 0;
        }}
        .object-title {{
            font-weight: 800;
        }}
        .pill {{
            display: inline-flex;
            align-items: center;
            min-height: 26px;
            padding: 4px 9px;
            border-radius: 999px;
            background: #e9f3ee;
            color: var(--green-dark);
            font-size: 12px;
            font-weight: 800;
        }}
        form {{
            background: var(--panel);
            padding: 20px;
            border: 1px solid var(--line);
            border-radius: 8px;
            max-width: 760px;
        }}
        input, select, textarea {{
            width: 100%;
            box-sizing: border-box;
            padding: 10px;
            margin-top: 6px;
            border: 1px solid #c9d6d0;
            border-radius: 6px;
            background: #fbfdfc;
        }}
        label {{
            display: block;
            margin: 13px 0;
            font-weight: 700;
        }}
        .alert {{
            padding: 12px;
            border-radius: 6px;
            background: #fff5dc;
            color: #694a00;
            border: 1px solid #eed496;
        }}
        .detail {{
            max-width: 760px;
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 18px;
        }}
        @media (max-width: 820px) {{
            .shell {{
                display: block;
            }}
            aside {{
                padding: 16px;
            }}
            nav {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            main {{
                padding: 20px 14px;
            }}
            .topbar {{
                display: block;
            }}
        }}
    </style>
</head>
<body>
    <div class="shell">
        <aside>
            <a class="brand" href="{BASE_URL}/">Cabanas Django</a>
            <p class="subtitle">Panel Python para gestionar apps, datos y vistas del sistema.</p>
            <nav>{nav_links}</nav>
        </aside>
        <main>
            <div class="topbar">
                <div>
                    <div class="eyebrow">Administracion</div>
                    <h1>{safe_title}</h1>
                    <p class="lead">Panel de administracion para el sistema de cabanas.</p>
                </div>
                <a class="button" href="/">Inicio</a>
            </div>
            {contenido}
        </main>
    </div>
</body>
</html>"""
    return HttpResponse(html)


def panel(request: HttpRequest) -> HttpResponse:
    """Botones principales, uno por app."""
    del request
    modulos = "".join(
        f"""
        <a class="module" href="{BASE_URL}/{escape(slug)}/">
            <strong>{escape(config["titulo"])}</strong>
            <span>Gestion del modulo {escape(config["titulo"])}.</span>
        </a>
        """
        for slug, config in CRUD_APPS.items()
    )
    contenido = f"""
    <div class="statbar">
        <div class="stat"><b>{len(CRUD_APPS)}</b><span>Modulos</span></div>
        <div class="stat"><b>Cabanas</b><span>Sistema</span></div>
    </div>
    <div class="grid">{modulos}</div>
    """
    return render_python("Panel de apps", contenido)


def listar(request: HttpRequest, app_slug: str) -> HttpResponse:
    """Boton Listar."""
    config = CRUD_APPS[app_slug]
    db_error = ""
    try:
        objetos = config["modelo"].objects.all()
    except (OperationalError, ProgrammingError):
        objetos = []
        db_error = "Falta crear o corregir la tabla de esta app con migraciones."
    filas = ""
    total = 0
    for objeto in objetos:
        total += 1
        pk = escape(str(objeto.pk))
        filas += f"""
            <tr>
                <td><span class="pill">#{pk}</span></td>
                <td><span class="object-title">{escape(str(objeto))}</span></td>
                <td>
                    <a class="button" href="{BASE_URL}/{escape(app_slug)}/{pk}/">Ver</a>
                    <a class="button" href="{BASE_URL}/{escape(app_slug)}/{pk}/editar/">Editar</a>
                    <a class="button danger" href="{BASE_URL}/{escape(app_slug)}/{pk}/borrar/">Borrar</a>
                </td>
            </tr>
        """
    if not filas:
        filas = '<tr><td colspan="3">No hay registros todavia.</td></tr>'
    alerta = f'<p class="alert">{escape(db_error)}</p>' if db_error else ""
    contenido = f"""
    <div class="statbar">
        <div class="stat"><b>{total}</b><span>Registros en {escape(config["titulo"])}</span></div>
        <div class="stat"><b>{escape(app_slug)}</b><span>Modulo activo</span></div>
    </div>
    <div class="toolbar">
        <a class="button" href="{BASE_URL}/">Panel</a>
        <a class="button primary" href="{BASE_URL}/{escape(app_slug)}/crear/">Crear</a>
    </div>
    {alerta}
    <div class="table-wrap">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Objeto</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {filas}
            </tbody>
        </table>
    </div>
    """
    return render_python(f"Cabanas - {config['titulo']}", contenido)


def crear(request: HttpRequest, app_slug: str) -> HttpResponse:
    """Boton Crear."""
    config = CRUD_APPS[app_slug]
    form_class = modelform_factory(config["modelo"], fields=config["campos"])
    form = form_class(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(f"{BASE_URL}/{app_slug}/")
    contenido = f"""
    <h2>Crear {escape(config["titulo"])}</h2>
    <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{escape(get_token(request))}">
        {form.as_p()}
        <div class="toolbar">
            <button class="button primary" type="submit">Guardar</button>
            <a class="button" href="{BASE_URL}/{escape(app_slug)}/">Cancelar</a>
        </div>
    </form>
    """
    return render_python(f"Cabanas - crear {config['titulo']}", contenido)


def ver(request: HttpRequest, app_slug: str, pk: int) -> HttpResponse:
    """Boton Ver."""
    config = CRUD_APPS[app_slug]
    objeto = get_object_or_404(config["modelo"], pk=pk)
    pk = escape(str(objeto.pk))
    contenido = f"""
    <div class="detail">
        <h2>Detalle de {escape(config["titulo"])}</h2>
        <p><strong>ID:</strong> <span class="pill">#{pk}</span></p>
        <p><strong>Objeto:</strong> {escape(str(objeto))}</p>
    </div>
    <div class="toolbar">
        <a class="button" href="{BASE_URL}/{escape(app_slug)}/">Listar</a>
        <a class="button primary" href="{BASE_URL}/{escape(app_slug)}/{pk}/editar/">Editar</a>
        <a class="button danger" href="{BASE_URL}/{escape(app_slug)}/{pk}/borrar/">Borrar</a>
    </div>
    """
    return render_python(f"Cabanas - ver {config['titulo']}", contenido)


def editar(request: HttpRequest, app_slug: str, pk: int) -> HttpResponse:
    """Boton Editar."""
    config = CRUD_APPS[app_slug]
    objeto = get_object_or_404(config["modelo"], pk=pk)
    form_class = modelform_factory(config["modelo"], fields=config["campos"])
    form = form_class(request.POST or None, instance=objeto)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(f"{BASE_URL}/{app_slug}/")
    contenido = f"""
    <h2>Editar {escape(config["titulo"])}</h2>
    <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{escape(get_token(request))}">
        {form.as_p()}
        <div class="toolbar">
            <button class="button primary" type="submit">Guardar</button>
            <a class="button" href="{BASE_URL}/{escape(app_slug)}/">Cancelar</a>
        </div>
    </form>
    """
    return render_python(f"Cabanas - editar {config['titulo']}", contenido)


def borrar(request: HttpRequest, app_slug: str, pk: int) -> HttpResponse:
    """Boton Borrar."""
    config = CRUD_APPS[app_slug]
    objeto = get_object_or_404(config["modelo"], pk=pk)
    if request.method == "POST":
        objeto.delete()
        return redirect(f"{BASE_URL}/{app_slug}/")
    contenido = f"""
    <h2>Borrar {escape(config["titulo"])}</h2>
    <p>Vas a borrar: <strong>{escape(str(objeto))}</strong></p>
    <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{escape(get_token(request))}">
        <div class="toolbar">
            <button class="button danger primary" type="submit">Confirmar borrado</button>
            <a class="button" href="{BASE_URL}/{escape(app_slug)}/">Cancelar</a>
        </div>
    </form>
    """
    return render_python(f"Cabanas - borrar {config['titulo']}", contenido)
