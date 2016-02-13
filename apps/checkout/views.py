from oscar.apps.checkout.views import PaymentDetailsView as _PaymentDetailsView

from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class PaymentDetailsView(_PaymentDetailsView):

    def post(self, request, *args, **kwargs):
        print("\n Preview disabilitata")
        return redirect(reverse('checkout:payment-details'))

