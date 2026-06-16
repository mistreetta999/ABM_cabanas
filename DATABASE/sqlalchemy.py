# cabanas_project/DATABASE/sqlalchemy.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Usa una variable de entorno para la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///./db.sqlite3")

# Crear motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos
Base = declarative_base()
