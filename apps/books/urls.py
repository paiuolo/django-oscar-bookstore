from django.conf.urls import patterns, url

from .views import AuthorDetail, AuthorList, BookStoreDetail, BookStoreList#, NewsletterSubscriptionView, SendToEmailView 

urlpatterns = patterns('',
    url(r'^authors/$', AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author_detail'),
    
    url(r'^bookstores/$', BookStoreList.as_view(), name='bookstore_list'),
    url(r'^bookstores/(?P<pk>\d+)/$', BookStoreDetail.as_view(), name='bookstore_detail'),
    
)
