""""leer venv"""
import os
from dotenv import load_dotenv

def load_env():
    """def leer"""
    load_dotenv()
    return {
        "SECRET_KEY": os.getenv("SECRET_KEY", "dummy-secret-key"),
        "DEBUG": os.getenv("DEBUG", "True") == "True",
    }
