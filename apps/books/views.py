from django.shortcuts import render

from django.views.generic import DetailView, ListView, View, TemplateView
from django.views.generic.edit import FormView

from .models import Author, BookStore

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from oscar.apps.order.models import Order



class AuthorDetail(DetailView):
    model = Author
    template_name = 'books/author_detail.html'

class AuthorList(ListView):
    model = Author
    template_name = 'books/author_list.html'



class BookStoreDetail(DetailView):
    model = BookStore
    template_name = 'books/bookstore_detail.html'

class BookStoreList(ListView):
    model = BookStore
    template_name = 'books/bookstore_list.html'


