@echo off
cd C:\Users\carol\OneDrive\Desktop\cabanas
call .venv\Scripts\activate.bat
python cabanas\django_core\__init_db.py
python manage.py runserver 127.0.0.1:8000
