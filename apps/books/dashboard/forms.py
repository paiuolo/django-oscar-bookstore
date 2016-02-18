from django import forms
from apps.books.models import Author, Serie, BookFormat, BookStore
from oscar.forms.widgets import ImageInput

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = []

class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        exclude = []
        
class BookFormatForm(forms.ModelForm):

    class Meta:
        model = BookFormat
        exclude = []

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStore
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super(BookStoreForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = "no-widget-init"