from django.db import connection
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

def clear_migrations():
    with connection.cursor() as cursor:
        print("Limpando migrações antigas...")
        cursor.execute("DELETE FROM django_migrations WHERE app = 'multas';")
        print("Migrações limpas com sucesso!")

if __name__ == "__main__":
    clear_migrations()
