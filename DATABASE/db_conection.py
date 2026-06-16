# base_datos/db_conection.py
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

class DotEnvConnection:
    """
    Clase para manejar la conexión a la base de datos
    usando variables de entorno definidas en .env
    """

    def __init__(self):
        self.engine = os.getenv("DB_ENGINE", "django.db.backends.sqlite3")
        self.name = os.getenv("DB_NAME", BASE_DIR / "db.sqlite3")
        self.user = os.getenv("DB_USER", "")
        self.password = os.getenv("DB_PASSWORD", "")
        self.host = os.getenv("DB_HOST", "")
        self.port = os.getenv("DB_PORT", "")

    def get_database_config(self):
        return {
            "default": {
                "ENGINE": self.engine,
                "NAME": self.name,
                "USER": self.user,
                "PASSWORD": self.password,
                "HOST": self.host,
                "PORT": self.port,
            }
        }







# Declarative Base para modelos
Base = declarative_base()


class db_conection:
    def __init__(self):
        self.database_url = get_database_url()


def get_database_url():
    """
    Retorna la URL de conexión según el motor elegido.
    Usa la variable DATABASE_URL en .env
    Ejemplos:
      - sqlite:///db.sqlite3
      - postgresql://user:password@localhost:5432/cabanas
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        # fallback a SQLite local
        db_url = f"sqlite:///{BASE_DIR}/db.sqlite3"
    return db_url

# Crear engine y sesión
DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    """
    Inicializa las tablas en la base de datos.
    """
    Base.metadata.create_all(bind=engine)


class load_dotenv:
    pass
