# cabanas_project/DATABASE/dotnet.py
from pathlib import Path

class load_dotenv:
    def __init__(self):
        pass
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
