from oscar.apps.partner import strategy, prices, availability
from decimal import Decimal as D


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        return Default()



class Default(strategy.UseFirstStockRecord, strategy.NoTax,
                 strategy.StockRequired, strategy.Structured):
    pass

class USStrategy(strategy.UseFirstStockRecord, strategy.DeferredTax,
                 strategy.StockRequired, strategy.Structured):
    pass
    
class BRStrategy(strategy.UseFirstStockRecord, strategy.FixedRateTax,
                 strategy.StockRequired, strategy.Structured):
    rate = D('0.04')