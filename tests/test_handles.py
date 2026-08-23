"""tests/test_handles.py

Tests for the view functions defined in:
  - interfaz_gestion_cabanas/handles.py
  - django_core/gestion_cabanas/handles.py  (referenced by the comment in that file)

These tests use django.test.RequestFactory + django.test.TestCase to call each
view function directly and assert that:
  1. The returned object is an HttpResponse with status_code == 200.
  2. The correct template name was used to render the response.

Calling the view functions directly (rather than going through the URL conf)
avoids the problem that the project's urlpatterns files only `include()`
other url modules without ever wiring these specific functions to a route.
"""
from django.test import RequestFactory, TestCase

from cabanas_apps.interfaz_gestion_cabanas import handles as handles_iface
from django_core.gestion_cabanas import handles as handlers_core


# ---------------------------------------------------------------------------
# Map:  (callable, expected_template_name)
# Adjust this list if you rename Templates or add more view functions.
# ---------------------------------------------------------------------------
INTERFAZ_VIEWS = [
    (handles_iface.pagina_principal_html, "pagina_principal.html"),
    (handles_iface.Formularios_panel_Django, "formularios/panel.html"),
    (handles_iface.imagen_panel_Django, "imagenes/panel.html"),
    (handles_iface.cabanas_panel_Django, "cabanas/panel.html"),
    (handles_iface.reservas_panel_Django, "reservas/panel.html"),
    (handles_iface.alquileres_panel_Django, "alquileres/panel.html"),
    (handles_iface.chatbot_panel_Django, "chatbot/panel.html"),
    (handles_iface.registros_panel_Django, "registros/panel.html"),
    (handles_iface.clientes_panel_Django, "clientes/panel.html"),
    (handles_iface.pagos_panel_Django, "pagos/panel.html"),
]

CORE_VIEWS = [
    (handles_core.pagina_principal, "pagina_principal.html"),
    (handles_core.cabanas_panel, "cabanas/panel.html"),
    (handles_core.reservas_panel, "reservas/panel.html"),
    (handles_core.chatbot_panel, "chatbot/panel.html"),
]


class HandlesViewsTests(TestCase):
    """Verifies every view in handles.py returns 200 and uses its template."""

    def setUp(self):
        self.factory = RequestFactory()

    def _assert_view(self, view, expected_template):
        request = self.factory.get("/")
        response = view(request)

        # 1. Status code check
        self.assertEqual(response.status_code, 200)

        # 2. Template check (works for both TemplateResponse and HttpResponse)
        self.assertIn(expected_template, response.template_name)


    # --- interfaz_gestion_cabanas/handles.py ---------------------------------
    def test_pagina_principal_html(self):
        self._assert_view(*INTERFAZ_VIEWS[0])

    def test_formularios_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[1])

    def test_imagen_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[2])

    def test_cabanas_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[3])

    def test_reservas_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[4])

    def test_alquileres_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[5])

    def test_chatbot_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[6])

    def test_registros_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[7])

    def test_clientes_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[8])

    def test_pagos_panel_django(self):
        self._assert_view(*INTERFAZ_VIEWS[9])

    # --- django_core/gestion_cabanas/handles.py -----------------------------
    def test_core_pagina_principal(self):
        self._assert_view(*CORE_VIEWS[0])

    def test_core_cabanas_panel(self):
        self._assert_view(*CORE_VIEWS[1])

    def test_core_reservas_panel(self):
        self._assert_view(*CORE_VIEWS[2])

    def test_core_chatbot_panel(self):
        self._assert_view(*CORE_VIEWS[3])

    # --- Smoke test: every view in both modules returns 200 -----------------
    def test_all_interfaz_views_return_200(self):
        for view, _tpl in INTERFAZ_VIEWS:
            with self.subTest(view=view.__name__):
                self.assertEqual(view(self.factory.get("/")).status_code, 200)

    def test_all_core_views_return_200(self):
        for view, _tpl in CORE_VIEWS:
            with self.subTest(view=view.__name__):
                self.assertEqual(view(self.factory.get("/")).status_code, 200)
