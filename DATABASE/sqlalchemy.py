"""Módulo de conexión con SQLAlchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite3")

# Crear motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear sesión
SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos
Base = declarative_base()

def get_db():
    """Devuelve una sesión de base de datos"""
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()
