from django import forms
from django.utils.translation import ugettext_lazy as _
from oscar.apps.dashboard.catalogue.forms import ProductForm as _ProductForm

from apps.catalogue.models import Product

class ProductForm(_ProductForm):
    class Meta:
        model = Product
        fields = ['title', 'upc', 'description', 'authors', 'translation_authors', 'serie', 'form', 'is_discountable', 'structure', 'background_color', 'file']
        
        widgets = {
            'structure': forms.HiddenInput(),
        }



