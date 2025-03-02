#!/bin/bash

# Executar migrações apenas para outras apps do Django
echo "Iniciando migrações..."
python manage.py migrate auth
python manage.py migrate admin
python manage.py migrate sessions
python manage.py migrate contenttypes

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Tentar importar dados
echo "Tentando importar dados..."
python manage.py importar_multas

# Iniciar o servidor Gunicorn
echo "Iniciando o servidor..."
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 