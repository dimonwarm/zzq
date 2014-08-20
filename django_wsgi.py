import os
import sys
import django.core.handlers.wsgi

if not os.path.dirname(__file__) in sys.path[:1]:
    sys.path.insert(0, os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'queryproject.queryproject.settings'
application = django.core.handlers.wsgi.WSGIHandler()
