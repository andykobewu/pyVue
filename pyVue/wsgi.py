"""
WSGI config for pyVue project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
#from some_asgi_library import AmazingMiddleware
#application = AmazingMiddleware(application)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyVue.settings')

application = get_wsgi_application()
