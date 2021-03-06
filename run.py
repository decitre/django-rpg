#!/usr/bin/env python
from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer
import sys
import os
import traceback
from django.core.management import call_command
from django.core.signals import got_request_exception
from rpg.wsgi import application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

def exception_printer(sender, **kwargs):
    traceback.print_exc()

got_request_exception.connect(exception_printer)

print 'Serving on 8088...'
WSGIServer(('', 8088), application).serve_forever()

