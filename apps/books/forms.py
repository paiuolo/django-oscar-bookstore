from django import forms
from .models import Author, Serie, BookFormat, BookStore


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = [
            'name', 'slug', 'description',
        ]

class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = [
            'name', 'slug', 'description',
        ]

class BookFormatForm(forms.ModelForm):

    class Meta:
        model = BookFormat
        fields = [
            'name', 'slug', 'virtual', 'description',
        ]

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStore
        fields = ['name', 'slug', 'description']
        
    def __init__(self, *args, **kwargs):
        super(BookStoreForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = "no-widget-init"