#!/bin/bash

# Coleta arquivos estáticos
python manage.py collectstatic --no-input

# Inicia o servidor
gunicorn mysite.wsgi 