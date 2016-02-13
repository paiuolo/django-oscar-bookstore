from oscar.apps.shipping.repository import Repository as _Repository
from oscar.apps.shipping import methods as shipping_methods
from decimal import Decimal as D

class Standard(shipping_methods.FixedPrice):
    code = 'standard'
    name = 'Standard shipping'
    charge_excl_tax = D('2.00')



class Repository(_Repository):

    methods = ( shipping_methods.Free(), )#, Standard() )
    

