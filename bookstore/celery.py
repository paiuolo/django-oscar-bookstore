from __future__ import absolute_import

import os

from celery import Celery

#setto il modulo settings di django come configurazione di celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

from django.conf import settings

app = Celery('bookstore')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


