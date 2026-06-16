from appcabanas.cabanas_models import Cabanas

# Usando la base por defecto (SQLite3)
cabanas_sqlite = Cabanas.objects.using('default').all()

# Usando PostgreSQL
cabanas_postgres = Cabanas.objects.using('postgresql').all()
