import os
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.translation import ugettext as _
from oscar.apps.customer.models import Email

from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')
Order = get_model('order', 'Order')
Line = get_model('order', 'Line')


def carica_lines_digitali(order):
    digital_lines = []
    for line in order.lines.all():
        if line.product.form:
            if line.product.form.slug in ['epub', 'mobi']:
                if line.product.file:
                    #digitali.append(line.product.file.path)
                    digital_lines.append(line)
    
    return digital_lines
    

def crea_email(order, email_address):
    email_subject = _('{0}, order #{1}'.format( settings.OSCAR_SHOP_NAME, order.number ))
    email_body = _('Attached order: {}. Thanks!'.format(order.number))
    email_sender = settings.OSCAR_FROM_EMAIL
    email_recepients = [email_address,]
    
    argom = [email_subject, email_body, email_sender, email_recepients]
    print('argomenti email', argom)
    email = EmailMessage( *argom )
    print('attributi email', dir(email))
    
    return email
    

def carica_allegati_email(email, digital_lines):
    for line in digital_lines:
        path = line.product.file.path
        print('attacco digitale', path)
        if(os.path.isfile(path)):
            email.attach_file(path)
            
            
def owned_products_pk(user):
    orders = Order.objects.filter(user=user)
    lines = Line.objects.none()
    products = set()
    for order in orders:
        lines = lines | order.lines.all()
    for line in lines:
        if line.product.digital_variants_aggregator:
            [products.add(p.pk) for p in line.product.digital_children]
        else:
            products.add(line.product.pk)
    return list(products)
    #return Product.objects.filter(pk__in=[p.pk for p in products])


"""
def owned_products_queryset(user):
    orders = Order.objects.filter(user=user)
        
    products = []
    for order in orders:
        for l in order.lines.all():
            products.append(l.product)
            
    pq = Product.objects.filter(id__in=[p.id for p in products])
    print('PQ',pq)
    return pq
"""


"""
def send_order_via_email(email_address, order):
    print('invio mail a ', email_address, 'per ordine', order)
    if email_address != "":    
        digital_lines = carica_lines_digitali(order)
        
        
        if len(digital_lines)>0:
            print('ttrovati', len(digital_lines), 'prodotti digitali', digital_lines)
            
            email = crea_email(order, email_address)
            carica_allegati_email(email, digital_lines)
            
            try:
                email.send()
            except:
                print('impossibile inviare email ordine, ', mail)
                return False
            else:
                print('email ordine inviata')
                for line in digital_lines:
                    line.set_status('Sent')
                
                if not order.is_anonymous:
                    email_oscar = Email.objects.create(user=order.user, subject=email.subject, body_text=email.body, body_html='<p>{}</p>'.format(email.body))                
                
                return True
        else:
            print('nessun file digitale')
            return False
    else:
        print('Nessun indirizzo email')
        return False
"""