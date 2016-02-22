from oscar.apps.offer import models, conditions, benefits, utils

from oscar.core.loading import get_class
from django.utils.translation import ugettext_noop as _

Product = get_class('catalogue.models', 'Product')


class AllProductsRange(object):
    name = _("All products")

    def contains_product(self, product):
        return product.is_virtual

    def num_products(self):
        return self.all_products().count()

    def all_products(self):
        return Product.objects.all()


class FreeTwinDigitalProducts(benefits.PercentageDiscountBenefit):
    description = _("Digital orders after the first are for free")
    
    class Meta:
        proxy = True

    def can_apply_benefit(self, line):
        twin_digital_products = line.basket.find_twin_digital_products()

        return line.stockrecord and line.product.is_discountable and (line.product in twin_digital_products)



class CheckTwinDigitalProducts(conditions.CoverageCondition):

    name = _("There are more than 1 variant of the same digital product")
    
    class Meta:
        proxy = True
        
    def is_satisfied(self, offer, basket):
        prodotto_fratello_pagato = False
        twin_digital_products = basket.find_twin_digital_products()
        
        for line in basket.lines.all():
            if line.product in twin_digital_products:
                prodotto_fratello_pagato = True
                break
                
        return prodotto_fratello_pagato



from oscar.apps.offer.models import *  # noqa
