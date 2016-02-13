from django.conf.urls import url, include
from oscar.apps.dashboard.app import DashboardApplication as _DashboardApplication

from apps.books.dashboard.app import application as BooksDashboardApplication


class DashboardApplication(_DashboardApplication):
    books_app = BooksDashboardApplication

    def get_urls(self):
        urls = super(DashboardApplication, self).get_urls()
        urls += [
            url(r'^books/', include(self.books_app.urls)),
        ]
        return self.post_process_urls(urls)


application = DashboardApplication()
