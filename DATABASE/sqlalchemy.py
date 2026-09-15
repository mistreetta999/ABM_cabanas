"""Módulo de conexión con SQLAlchemy"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la base de datos
DB_NAME = os.getenv("DB_NAME", "cabanas_db")
DB_USER = os.getenv("DB_USER", "carolina")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# URL de conexión (PostgreSQL por defecto, cambiar si usás SQLite u otro motor)
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear engine y sesión
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()


def get_db():
    """Devuelve una sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
