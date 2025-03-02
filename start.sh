#!/bin/bash

# Executar migrações
echo "Iniciando migrações..."
python manage.py makemigrations multas
python manage.py migrate

# Tentar importar dados
echo "Tentando importar dados..."
python manage.py importar_multas

# Iniciar o servidor Gunicorn
echo "Iniciando o servidor..."
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 