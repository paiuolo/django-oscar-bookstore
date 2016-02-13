from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from oscar.apps.customer.views import OrderDetailView as _OrderDetailView

#from apps.books.functions import send_order_via_email

from django.contrib import messages

from apps.books.tasks import send_order_via_email

class OrderDetailView(_OrderDetailView):

    def do_resend(self, order):
        send_order_via_email.apply_async((order.user.email, order.number), countdown=10)
        
        self.response = redirect('customer:order-list')
        messages.info(
                self.request,
                _("All available items from order %(number)s "
                    "have been sent to %(email)s") % {'number': order.number, 'email': order.user.email})
