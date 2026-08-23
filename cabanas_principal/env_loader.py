import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    return {
        "SECRET_KEY": os.getenv("SECRET_KEY", "dummy-secret-key"),
        "DEBUG": os.getenv("DEBUG", "True") == "True",
    }
