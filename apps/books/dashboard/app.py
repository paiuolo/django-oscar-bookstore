from django.conf.urls import url

from oscar.core.application import Application

from apps.books.dashboard.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, SerieListView, SerieCreateView, SerieUpdateView, SerieDeleteView, BookFormatListView, BookFormatCreateView, BookFormatUpdateView, BookFormatDeleteView, BookStoreListView, BookStoreCreateView, BookStoreUpdateView, BookStoreDeleteView

class BooksDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    author_list_view = AuthorListView
    author_create_view = AuthorCreateView
    author_update_view = AuthorUpdateView
    author_delete_view = AuthorDeleteView

    serie_list_view = SerieListView
    serie_create_view = SerieCreateView
    serie_update_view = SerieUpdateView
    serie_delete_view = SerieDeleteView
    
    bookformat_list_view = BookFormatListView
    bookformat_create_view = BookFormatCreateView
    bookformat_update_view = BookFormatUpdateView
    bookformat_delete_view = BookFormatDeleteView

    bookstore_list_view = BookStoreListView
    bookstore_create_view = BookStoreCreateView
    bookstore_update_view = BookStoreUpdateView
    bookstore_delete_view = BookStoreDeleteView



    def get_urls(self):
        urlpatterns = [
            url(r'^authors/$', self.author_list_view.as_view(), name='author-list'),
            url(r'^authors/create/$', self.author_create_view.as_view(), name='author-create'),
            url(r'^authors/(?P<pk>\d+)/$', self.author_update_view.as_view(),
                name='author-update'),
            url(r'^authors/(?P<pk>\d+)/delete/$', self.author_delete_view.as_view(),
                name='author-delete'),
            
            url(r'^serie/$', self.serie_list_view.as_view(), name='serie-list'),
            url(r'^serie/create/$', self.serie_create_view.as_view(), name='serie-create'),
            url(r'^serie/(?P<pk>\d+)/$', self.serie_update_view.as_view(),
                name='serie-update'),
            url(r'^serie/(?P<pk>\d+)/delete/$', self.serie_delete_view.as_view(),
                name='serie-delete'),
            
            url(r'^bookformat/$', self.bookformat_list_view.as_view(), name='bookformat-list'),
            url(r'^bookformat/create/$', self.bookformat_create_view.as_view(), name='bookformat-create'),
            url(r'^bookformat/(?P<pk>\d+)/$', self.bookformat_update_view.as_view(),
                name='bookformat-update'),
            url(r'^bookformat/(?P<pk>\d+)/delete/$', self.bookformat_delete_view.as_view(),
                name='bookformat-delete'),   

            url(r'^bookstore/$', self.bookstore_list_view.as_view(), name='bookstore-list'),
            url(r'^bookstore/create/$', self.bookstore_create_view.as_view(), name='bookstore-create'),
            url(r'^bookstore/(?P<pk>\d+)/$', self.bookstore_update_view.as_view(),
                name='bookstore-update'),
            url(r'^bookstore/(?P<pk>\d+)/delete/$', self.bookstore_delete_view.as_view(),
                name='bookstore-delete'),  
        ]
        return self.post_process_urls(urlpatterns)


application = BooksDashboardApplication()
