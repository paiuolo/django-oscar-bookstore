from __future__ import absolute_import # Celery no clashing with bookstore

from .celery import app as celery_app