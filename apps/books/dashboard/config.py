from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BooksDashboardConfig(AppConfig):
    label = 'books_dashboard'
    name = 'books.dashboard'
    verbose_name = _('Books dashboard')