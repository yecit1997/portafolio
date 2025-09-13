import os
import sys

path = '/home/yecit1997/portafolio' # Ruta a tu proyecto de Django
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings' # Reemplaza 'tu_proyecto' con el nombre real de tu proyecto

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import os
import sys

path = '/home/yecit1997/portafolio' # Ruta a tu proyecto de Django
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings' # Reemplaza 'tu_proyecto' con el nombre real de tu proyecto

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()