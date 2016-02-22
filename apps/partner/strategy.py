from oscar.apps.partner import strategy, prices, availability
from decimal import Decimal as D
from oscar.apps.partner import availability, prices

class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        #print('Assegno strategy', request, user)
        return BRStrategy()



class Default(strategy.UseFirstStockRecord, strategy.NoTax,
                 strategy.StockRequired, strategy.Structured):
    pass

class USStrategy(strategy.UseFirstStockRecord, strategy.DeferredTax,
                 strategy.StockRequired, strategy.Structured):
    pass
    

    
class BRStrategy(strategy.UseFirstStockRecord, strategy.FixedRateTax,
                 strategy.StockRequired, strategy.Structured):
    
    rate = D('0.04')
    
    def pricing_policy(self, product, stockrecord):
        #print('stockrecord', stockrecord)
        return super(BRStrategy, self).pricing_policy(product, stockrecord)
    
    