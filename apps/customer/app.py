from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from oscar.apps.customer.app import CustomerApplication as _CustomerApplication

from .views import PersonalLibraryView

class CustomerApplication(_CustomerApplication):
    
    personal_library_view = PersonalLibraryView
    
    def get_urls(self):
        urls = super(CustomerApplication, self).get_urls()
        urls += [
            url(r'^personal-library/',
                login_required(self.personal_library_view.as_view()),
                name='personal-library'),
        ]
        return self.post_process_urls(urls)


application = CustomerApplication()