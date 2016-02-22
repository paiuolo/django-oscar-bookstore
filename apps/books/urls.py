from django.conf.urls import patterns, url

from .views import AuthorDetail, AuthorList, BookStoreDetail, BookStoreList, SerieDetail, SerieList#, DigitalGoodDownload

urlpatterns = patterns('',
    url(r'^authors/$', AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<slug>[\w-]+)$', AuthorDetail.as_view(), name='author_detail'),
    
    url(r'^bookstores/$', BookStoreList.as_view(), name='bookstore_list'),
    url(r'^bookstores/(?P<pk>\d+)/$', BookStoreDetail.as_view(), name='bookstore_detail'),
    
    url(r'^series/$', SerieList.as_view(), name='serie_list'),
    url(r'^series/(?P<slug>[\w-]+)$', SerieDetail.as_view(), name='serie_detail'),
    
    #url(r'^digital_goods/(?P<pk>\d+)/', DigitalGoodDownload.as_view(), name='digital_good_download')
    
)
