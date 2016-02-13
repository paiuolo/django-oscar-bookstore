from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ungettext, ugettext_lazy as _
from django.views.generic import (
    ListView, DeleteView, CreateView, UpdateView, View)


from oscar.views.generic import BulkEditMixin
from oscar.core.loading import get_classes, get_model

from apps.books.models import Author, Serie, BookFormat, BookStore
from apps.books.forms import AuthorForm, SerieForm, BookFormatForm, BookStoreForm

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'books/dashboard/author_list.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'books/dashboard/author_form.html'
    form_class = AuthorForm

    def get_success_url(self):
        messages.warning(self.request, _("Author created"))
        return reverse('dashboard:author-list')

    def get_context_data(self, **kwargs):
        ctx = super(AuthorCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create author")
        return ctx


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'books/dashboard/author_form.html'
    form_class = AuthorForm

    def get_object(self):
        obj = super(AuthorUpdateView, self).get_object()
        return obj

    def get_success_url(self):
        messages.warning(self.request, _("Author updated"))
        return reverse('dashboard:author-list')

    def get_context_data(self, **kwargs):
        ctx = super(AuthorUpdateView, self).get_context_data(**kwargs)
        ctx['author'] = self.object
        ctx['title'] = self.object.name
        return ctx


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'books/dashboard/author_delete.html'
    context_object_name = 'author'

    def get_success_url(self):
        messages.warning(self.request, _("Author deleted"))
        return reverse('dashboard:author-list')


class SerieListView(ListView):
    model = Serie
    context_object_name = 'serie'
    template_name = 'books/dashboard/series_list.html'


class SerieCreateView(CreateView):
    model = Serie
    template_name = 'books/dashboard/series_form.html'
    form_class = SerieForm

    def get_success_url(self):
        messages.warning(self.request, _("Serie created"))
        return reverse('dashboard:serie-list')

    def get_context_data(self, **kwargs):
        ctx = super(SerieCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create series")
        return ctx


class SerieUpdateView(UpdateView):
    model = Serie
    template_name = 'books/dashboard/series_form.html'
    form_class = SerieForm

    def get_object(self):
        obj = super(SerieUpdateView, self).get_object()
        return obj

    def get_success_url(self):
        messages.warning(self.request, _("Serie updated"))
        return reverse('dashboard:serie-list')

    def get_context_data(self, **kwargs):
        ctx = super(SerieUpdateView, self).get_context_data(**kwargs)
        ctx['series'] = self.object
        ctx['title'] = self.object.name
        return ctx


class SerieDeleteView(DeleteView):
    model = Serie
    template_name = 'books/dashboard/series_delete.html'
    context_object_name = 'serie'

    def get_success_url(self):
        messages.warning(self.request, _("Serie deleted"))
        return reverse('dashboard:serie-list')
    

class BookFormatListView(ListView):
    model = BookFormat
    context_object_name = 'bookformats'
    template_name = 'books/dashboard/bookformat_list.html'


class BookFormatCreateView(CreateView):
    model = BookFormat
    template_name = 'books/dashboard/bookformat_form.html'
    form_class = BookFormatForm

    def get_success_url(self):
        messages.warning(self.request, _("Bookformat created"))
        #return reverse('dashboard:bookformat-list')
        return reverse('dashboard:bookformat-list')

    def get_context_data(self, **kwargs):
        ctx = super(BookFormatCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create bookformat")
        return ctx


class BookFormatUpdateView(UpdateView):
    model = BookFormat
    template_name = 'books/dashboard/bookformat_form.html'
    form_class = BookFormatForm

    def get_object(self):
        obj = super(BookFormatUpdateView, self).get_object()
        return obj

    def get_success_url(self):
        messages.warning(self.request, _("Bookformat updated"))
        return reverse('dashboard:bookformat-list')

    def get_context_data(self, **kwargs):
        ctx = super(BookFormatUpdateView, self).get_context_data(**kwargs)
        ctx['bookformat'] = self.object
        ctx['title'] = self.object.name
        return ctx


class BookFormatDeleteView(DeleteView):
    model = BookFormat
    template_name = 'books/dashboard/bookformat_delete.html'
    context_object_name = 'bookformat'

    def get_success_url(self):
        messages.warning(self.request, _("Bookformat deleted"))
        return reverse('dashboard:bookformat-list')
    
    

    
class BookStoreListView(ListView):
    model = BookStore
    context_object_name = 'bookstores'
    template_name = 'books/dashboard/bookstore_list.html'


class BookStoreCreateView(CreateView):
    model = BookStore
    template_name = 'books/dashboard/bookstore_form.html'
    form_class = BookStoreForm

    def get_success_url(self):
        messages.warning(self.request, _("Bookstore created"))
        #return reverse('dashboard:bookstore-list')
        return reverse('dashboard:bookstore-list')

    def get_context_data(self, **kwargs):
        ctx = super(BookStoreCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create bookstore")
        return ctx


class BookStoreUpdateView(UpdateView):
    model = BookStore
    template_name = 'books/dashboard/bookstore_form.html'
    form_class = BookStoreForm

    def get_object(self):
        obj = super(BookStoreUpdateView, self).get_object()
        return obj

    def get_success_url(self):
        messages.warning(self.request, _("Bookstore updated"))
        return reverse('dashboard:bookstore-list')

    def get_context_data(self, **kwargs):
        ctx = super(BookStoreUpdateView, self).get_context_data(**kwargs)
        ctx['bookstore'] = self.object
        ctx['title'] = self.object.name
        return ctx


class BookStoreDeleteView(DeleteView):
    model = BookStore
    template_name = 'books/dashboard/bookstore_delete.html'
    context_object_name = 'bookstore'

    def get_success_url(self):
        messages.warning(self.request, _("Bookstore deleted"))
        return reverse('dashboard:bookstore-list')
    