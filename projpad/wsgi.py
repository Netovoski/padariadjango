"""
WSGI config for projpad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, seed
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projpad.settings')

application = get_wsgi_application()
