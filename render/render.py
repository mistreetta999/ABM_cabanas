""""Este archivo contiene la configuración de la aplicación FastAPI para Render."""
import os
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn

class RenderApp:
    """ class RenderApp para la configuración de la aplicación FastAPI en Render."""
    def __init__(self):
        # Cargar variables de entorno desde .env
        load_dotenv()

        # Inicializar FastAPI
        self.app = FastAPI(title="Cabana API")

        # Configurar rutas
        self._configure_routes()

    def _configure_routes(self):
        @self.app.get("/")
        def root():
            return {"message": "Cabana API funcionando en Render"}

    def run(self:RenderApp)->None:
        """Arranca la aplicación FastAPI en Render."""
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", "8080"))

        uvicorn.run(self.app, host=host, port=port)

# Punto de entrada
if __name__ == "__main__":
    app_instance = RenderApp()
    app_instance.run()
