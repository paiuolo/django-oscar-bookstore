from django import forms
from django.utils.translation import ugettext_lazy as _
from oscar.apps.basket.forms import AddToBasketForm as _AddToBasketForm


class AddToBasketForm(_AddToBasketForm):
    
    def clean_quantity(self):
        current_qty = self.basket.product_quantity(self.product)
        desired_qty = current_qty + self.cleaned_data.get('quantity', 1)
        
        if self.parent_product.is_virtual and desired_qty > 1:        
            raise forms.ValidationError(
                _("You are only allowed to purchase a maximum of 1 of these."))

        return super(AddToBasketForm, self).clean_quantity()


