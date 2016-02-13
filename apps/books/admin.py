from django.contrib import admin

from .models import Author, Serie, BookFormat, BookStore

admin.site.register(Author)
admin.site.register(Serie)
admin.site.register(BookFormat)
admin.site.register(BookStore)