from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from oscar.apps.customer.views import OrderDetailView as _OrderDetailView

from django.contrib import messages
from django.views import generic

from apps.books.tasks import send_order_via_email

from django.conf import settings

from oscar.core.loading import get_model, get_class

from itertools import chain

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

Order = get_model('order', 'Order')
Product = get_model('catalogue', 'Product')
PageTitleMixin = get_class('customer.mixins', 'PageTitleMixin')

from apps.books.forms import DigitalDownloadForm

from apps.books.functions import owned_products_pk

from django.conf import settings

class OrderDetailView(_OrderDetailView):

    def do_resend(self, order):
        if settings.CELERY_IS_ACTIVE:
            send_order_via_email.apply_async((order.user.email, order.number), countdown=10)
        else:
            send_order_via_email(order.user.email, order.number)
        
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
    form_class = DigitalDownloadForm

    def get_queryset(self):
        orders = self.model._default_manager.filter(user=self.request.user)
        
        products = []
        for order in orders:
            for l in order.lines.all():
                products.append(l.product)
        
        return products
    
    def post(self, request, *args, **kwargs):
        print('\n post', request.POST)
        product_id = int(request.POST.get('product_id'))
        owned_products_id = owned_products_pk(request.user)
        print('product_id owned?', product_id, owned_products_id,product_id in owned_products_id, type(product_id), type(owned_products_id[0]) )
        if product_id in owned_products_id:
            product = Product.objects.get(id=product_id)
            response = HttpResponse()
            url = "/books/virtual_store/{}",format(product.file.name)
            print('redirect to url', url)
            response['X-Accel-Redirect'] = url
            return response
        
        return HttpResponseRedirect(reverse('customer:personal-library'))
        
        messages.info(
                self.request,
                "Product not owned")


