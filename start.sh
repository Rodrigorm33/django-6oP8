#!/bin/bash

# Aplica as migrações do banco de dados
python manage.py migrate --no-input

# Coleta arquivos estáticos
python manage.py collectstatic --no-input

# Inicia o servidor
gunicorn mysite.wsgi --log-file - 