import os, sys
sys.path.append('/home/django/kr0k3n')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kr0k3n.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
