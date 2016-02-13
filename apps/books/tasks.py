from __future__ import absolute_import

from celery import shared_task

from oscar.apps.customer.models import Email
from oscar.core.loading import get_class

from .functions import carica_lines_digitali, carica_allegati_email, crea_email

ShippingEventType = get_class('order.models', 'ShippingEventType')
Order = get_class('order.models', 'Order')



@shared_task
def send_order_via_email(email_address, order_number):
    assert(email_address!='')
    print('Cerco ordine', order_number)
    
    order = Order.objects.get(number=order_number)
    
    print('invio mail a ', email_address, 'per ordine', order)
    
    order.set_status('Being processed')
    
    order_sent = False
    ordine_fisico = order.basket.is_shipping_required()
    
    digital_lines = carica_lines_digitali(order)
    
    if len(digital_lines)>0:
        print('ttrovati', len(digital_lines), 'prodotti digitali', digital_lines)
        
        email = crea_email(order, email_address)
        carica_allegati_email(email, digital_lines)
        
        try:
            email.send()
        except:
            print('impossibile inviare email ordine, ', mail)
        else:
            print('email ordine inviata')
            for line in digital_lines:
                line.set_status('Sent')
            
            if not order.is_anonymous:
                email_oscar = Email.objects.create(user=order.user, subject=email.subject, body_text=email.body, body_html='<p>{}</p>'.format(email.body))                
            
            order_sent = True
    else:
        print('nessun file digitale')
    
    if order_sent:
        print('\n Ordine inviato', order)
        event_type, __ = ShippingEventType.objects.get_or_create(name="Email")
        
        event = order.shipping_events.create(
            event_type=event_type, notes='Sent to {}'.format(email_address))
    else:
        print('\n Ordine NON inviato', order)
    
    if order_sent and not ordine_fisico:
            order.set_status('Sent')
