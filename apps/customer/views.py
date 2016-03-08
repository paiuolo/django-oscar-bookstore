from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from oscar.apps.customer.views import OrderDetailView as _OrderDetailView

from django.contrib import messages
from django.views import generic

from apps.books.tasks import send_order_via_email

from django.conf import settings

from oscar.core.loading import get_model, get_class

from itertools import chain

Order = get_model('order', 'Order')
Product = get_model('catalogue', 'Product')
PageTitleMixin = get_class('customer.mixins', 'PageTitleMixin')


class OrderDetailView(_OrderDetailView):

    def do_resend(self, order):
        send_order_via_email.apply_async((order.user.email, order.number), countdown=10)
        
        self.response = redirect('customer:order-list')
        messages.info(
                self.request,
                _("All available items from order %(number)s "
                    "have been sent to %(email)s") % {'number': order.number, 'email': order.user.email})



class PersonalLibraryView(PageTitleMixin, generic.ListView):
    """
    Customer personal library
    """
    
    context_object_name = "products"
    template_name = 'customer/personal_library.html'
    paginate_by = settings.OSCAR_ORDERS_PER_PAGE
    model = Order
    page_title = _('Personal Library')
    active_tab = 'personal-library'

    def get_queryset(self):
        orders = self.model._default_manager.filter(user=self.request.user)
        
        products = []
        for order in orders:
            for l in order.lines.all():
                products.append(l.product)
        
        return products


