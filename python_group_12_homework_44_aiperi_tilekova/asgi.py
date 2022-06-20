"""
ASGI config for python_group_12_homework_44_aiperi_tilekova project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_group_12_homework_44_aiperi_tilekova.settings')

application = get_asgi_application()