from django import forms

from oscar.core.compat import existing_user_fields, get_user_model
from oscar.core.loading import get_model

from .models import DigitalDownload

User = get_user_model()

Product = get_model('catalogue', 'Product')


class DigitalDownloadForm(forms.ModelForm):
    
    class Meta:
        model = DigitalDownload
        fields = ['user', 'product']
        
    def clean_product(self):
        product = self.cleaned_data['product']
        print('product', product)
        return product