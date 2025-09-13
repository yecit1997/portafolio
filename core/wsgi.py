"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()


import os
import sys

path = '/home/yecit1997/portafolio' # Ruta a tu proyecto de Django
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings' # Reemplaza 'tu_proyecto' con el nombre real de tu proyecto

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()