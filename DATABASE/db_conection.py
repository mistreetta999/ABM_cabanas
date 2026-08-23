# base_datos/db_conection.py
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
import os
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from pathlib import Path
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from dotenv import load_dotenv
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from sqlalchemy import create_engine
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from sqlalchemy.orm import declarative_base, sessionmaker
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
BASE_DIR = Path(__file__).resolve().parent.parent.parent
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
load_dotenv(BASE_DIR / ".env")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class DotEnvConnection:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Clase para manejar la conexión a la base de datos
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    usando variables de entorno definidas en .env
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __init__(self):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.engine = os.getenv("DB_ENGINE", "django.db.backends.sqlite3")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.name = os.getenv("DB_NAME", BASE_DIR / "db.sqlite3")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.user = os.getenv("DB_USER", "")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.password = os.getenv("DB_PASSWORD", "")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.host = os.getenv("DB_HOST", "")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.port = os.getenv("DB_PORT", "")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def get_database_config(self):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return {
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            "default": {
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
                "ENGINE": self.engine,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
                "NAME": self.name,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
                "USER": self.user,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
                "PASSWORD": self.password,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
                "HOST": self.host,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
                "PORT": self.port,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            }
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        }
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
# Declarative Base para modelos
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
Base = declarative_base()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class db_conection:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __init__(self):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.database_url = get_database_url()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def get_database_url():
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Retorna la URL de conexión según el motor elegido.
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Usa la variable DATABASE_URL en .env
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Ejemplos:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
      - sqlite:///db.sqlite3
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
      - postgresql://user:password@localhost:5432/cabanas
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    db_url = os.getenv("DATABASE_URL")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    if not db_url:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        # fallback a SQLite local
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        db_url = f"sqlite:///{BASE_DIR}/db.sqlite3"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return db_url
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
# Crear engine y sesión
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
DATABASE_URL = get_database_url()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
engine = create_engine(DATABASE_URL, echo=True, future=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def init_db():
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Inicializa las tablas en la base de datos.
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Base.metadata.create_all(bind=engine)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class load_dotenv:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    pass
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
