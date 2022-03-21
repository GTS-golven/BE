"""
WSGI config for BE project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('~/home/pi/gts/gts-be-test/login')

sys.path.append('~/home/pi/gts/gtsenv/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BE.settings')

application = get_wsgi_application()
