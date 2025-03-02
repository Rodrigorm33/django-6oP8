"""
WSGI config for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
import logging

from django.core.wsgi import get_wsgi_application

# Configuração de logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    application = get_wsgi_application()
    logger.info("Aplicação WSGI iniciada com sucesso")
except Exception as e:
    logger.error(f"Erro ao iniciar a aplicação WSGI: {str(e)}")
    logger.exception(e)
    raise
