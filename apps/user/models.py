from django.db import models
from django.utils.translation import ugettext_lazy as _

from oscar.apps.customer.abstract_models import AbstractUser

class User(AbstractUser):
    
    newsletter_subscribed = models.BooleanField(
        _('Newsletter subscribed'), default=True,
        help_text=_('Subscribe to our newsletter'))
    
    additional_fields = ['newsletter_subscribed']

