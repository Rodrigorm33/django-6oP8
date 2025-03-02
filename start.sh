#!/bin/bash

# Verifica variáveis de ambiente do banco de dados
if [ -z "$DATABASE_URL" ]; then
    if [ -n "$PGUSER" ] && [ -n "$PGPASSWORD" ] && [ -n "$PGHOST" ] && [ -n "$PGPORT" ] && [ -n "$PGDATABASE" ]; then
        export DATABASE_URL="postgresql://$PGUSER:$PGPASSWORD@$PGHOST:$PGPORT/$PGDATABASE"
        echo "DATABASE_URL construída a partir das variáveis PostgreSQL"
    else
        echo "Erro: DATABASE_URL não está definida e variáveis PostgreSQL estão incompletas"
        exit 1
    fi
fi

# Aguarda o banco de dados ficar disponível
echo "Aguardando conexão com o banco de dados..."
python manage.py wait_for_db

# Aplica as migrações do banco de dados
echo "Aplicando migrações..."
python manage.py migrate --no-input

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

# Inicia o servidor
echo "Iniciando o servidor Gunicorn..."
gunicorn mysite.wsgi --log-file -