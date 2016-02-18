from django import forms
from django.utils.translation import ugettext_lazy as _
from oscar.apps.dashboard.catalogue.forms import ProductForm as _ProductForm

from oscar.core.loading import get_class


Product = get_class('catalogue.models', 'Product')

from apps.books.models import BookFormat, Author


class ProductForm(_ProductForm):
    
    class Meta:
        model = Product
        fields = ['title', 'upc', 'description', 'authors', 'translation_authors', 'serie', 'form', 'is_discountable', 'structure', 'background_color', 'file', 'publication_date', 'number_of_pages']
        
        widgets = {
            'structure': forms.HiddenInput(),
        }
