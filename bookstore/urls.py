"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from oscar.app import application

from paypal.express.dashboard.app import application as paypal_application

from apps.sitemaps import base_sitemaps


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    url(r'^dashboard/paypal/express/', include(paypal_application.urls)),
    
    url(r'', include(application.urls)),
    
    url(r'^books/', include('apps.books.urls')),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    # sitemaps
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {
        'sitemaps': base_sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        'django.contrib.sitemaps.views.sitemap', {'sitemaps': base_sitemaps}),
    
]


from django.conf import settings
from django.conf.urls.static import static
from oscar.views import handler500, handler404, handler403

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
    ]
    
