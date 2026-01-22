"""
WSGI config for mysite project on PythonAnywhere.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/Poryz/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Use StaticFilesHandler for serving static files during development
application = StaticFilesHandler(get_wsgi_application())