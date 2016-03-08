from oscar.apps.offer.applicator import Applicator as _Applicator
from oscar.apps.offer.custom import create_range, create_benefit, create_condition

from oscar.core.loading import get_model
from django.utils.translation import ugettext_lazy as _

from .models import CheckTwinDigitalProducts, FreeTwinDigitalProducts, AllProductsRange

from django.conf import settings

Range = get_model('offer', 'Range')
CoverageCondition = get_model('offer', 'CoverageCondition')
PercentageDiscountBenefit = get_model('offer', 'PercentageDiscountBenefit')
ConditionalOffer = get_model('offer', 'ConditionalOffer')



def create_twin_product_offer():
    
    try:
        o1 = ConditionalOffer.objects.get(slug='remove-twin-products')
    except:
        print('Modelli offer non presenti, li creo')
        # creare range
        r = create_range(AllProductsRange)

        c1_new = True
        try:
            c1 = create_condition(CheckTwinDigitalProducts, range=r, value=1, type=CoverageCondition.COVERAGE)
        except:
            c1_new = False
            c1 = CheckTwinDigitalProducts.objects.get(range=r, value=1, type=CoverageCondition.COVERAGE)
        print('Check Preso?', c1, 'Nuovo?', c1_new)
        
        
        b1 = create_benefit(FreeTwinDigitalProducts, range=r, value=100, type=PercentageDiscountBenefit.PERCENTAGE)
        print('Benefit Preso?', b1)
        
        
        o1, o1_new= ConditionalOffer.objects.get_or_create(name='Remove twin products', condition=c1, benefit=b1, offer_type=ConditionalOffer.SESSION)
        print('Offer Preso?', o1, 'Nuova?', o1_new)
    
    return o1


class Applicator(_Applicator):

    def get_session_offers(self, request):
        if settings.CHECK_TWIN_DIGITAL_PRODUCTS:
            try:
                o1 = ConditionalOffer.objects.get(slug='remove-twin-products')
            except:
                o1 = create_twin_product_offer()
            
            return [o1,]
        return []