from django.db import connections, DEFAULT_DB_ALIAS

def get_db_connection(alias=DEFAULT_DB_ALIAS):
    return connections[alias]
