from django.utils.translation import ugettext_lazy as _

from oscar.apps.order.processing import EventHandler as _EventHandler
from oscar.apps.order.signals import order_placed
from oscar.apps.order.models import Order
from oscar.core.loading import get_class

#from apps.books.functions import send_order_via_email
from apps.books.tasks import send_order_via_email
from apps.books.models import DigitalGood

ShippingEventType = get_class('order.models', 'ShippingEventType')


class EventHandler(_EventHandler):
    
    def handle_order_status_change(self, order, new_status, note_msg=None):
        
        print("\nCambiato stato ordine:", new_status)
        
        super(EventHandler, self).handle_order_status_change(order, new_status, note_msg)
        
        
    def handle_payment_event(self, order, event_type, amount, lines=None,
                             line_quantities=None, **kwargs):
        
        print("\nEvento pagamento", event_type, amount)
        
        super(EventHandler, self).handle_payment_event(order, event_type, amount, lines, line_quantities, **kwargs)






def manage_order_after_payment(sender, **kwargs):
    print("\n Ordine piazzato!")
    
    _user = kwargs.get('user')
    order = kwargs.get('order')
    #print(_user, '\n', order, 'Order#', order.number)
    
    email_address = ""
    if order.is_anonymous:
        email_address = order.guest_email
    else:
        dg = DigitalGood.objects.get_or_create(order=order, user=_user)
        email_address = _user.email
    
    send_order_via_email.apply_async((email_address, order.number), countdown=10)
    
        
order_placed.connect(manage_order_after_payment)