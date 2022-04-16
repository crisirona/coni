"""
WSGI config for staticproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys


project_home = '/home/crissirona/conipage'
if project_home not in sys.path:
    sys.path.insert(0,project_home)

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE']= 'staticproject.settings'

application = get_wsgi_application()
