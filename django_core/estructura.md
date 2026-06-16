# Estructura Django

```text
cabanas/
|-- manage.py
|-- main.py
|-- cabanas_project/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- asgi.py
|-- cabana_apps/
|   |-- models.py
|   |-- forms.py
|   |-- views.py
|   `-- urls.py
|-- chatbot/
|   |-- views.py
|   `-- urls.py
`-- Template/
    |-- pagina_principal.html
    |-- base.html
    |-- cabana_apps/
    `-- chatbot/
```
*** Update File: cabana_apps/views.py
@@
 class InicioView(TemplateView):
     template_name = 'pagina_principal.html'
 
 
 class PanelView(TemplateView):
     template_name = 'cabana_apps/panel.html'
 
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['clientes_count'] = Cliente.objects.count()
         context['cabanas_count'] = Cabana.objects.count()
         context['reservas_count'] = Reserva.objects.count()
         return context
