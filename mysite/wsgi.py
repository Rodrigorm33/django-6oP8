"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import subprocess
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

try:
    # Executar migrações da app multas primeiro
    subprocess.run(['python', 'manage.py', 'makemigrations', 'multas'])
    
    # Executar todas as migrações
    subprocess.run(['python', 'manage.py', 'migrate'])
    
    # Executar importação de dados
    subprocess.run(['python', 'manage.py', 'importar_multas'])
except Exception as e:
    print(f"Erro durante a inicialização: {str(e)}")

application = get_wsgi_application()
