DEBUG = False  # Desabilita modo debug em produção

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'django-server-production-a20e.up.railway.app',
    '.railway.app',
    '*',
]

# Configurações adicionais de segurança
CSRF_TRUSTED_ORIGINS = [
    'https://django-server-production-a20e.up.railway.app',
    'https://*.railway.app',
]
