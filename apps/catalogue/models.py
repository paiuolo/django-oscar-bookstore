from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.apps.catalogue.abstract_models import AbstractProduct

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

from apps.books.models import Author, Serie, BookFormat, BookStore

from django.utils import timezone
from datetime import timedelta

from django.db.models import Q

#storage_magazzino_virtuale = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'magazzino_virtuale'))
storage_magazzino_virtuale = FileSystemStorage(location='/srv/django-oscar-bookstore/digital_products/')

class Product(AbstractProduct):
    
    authors = models.ManyToManyField(
        Author, blank=True, related_name='books', verbose_name=_("authors"))
    
    bookstores = models.ManyToManyField(
        BookStore, blank=True, related_name='books', verbose_name=_("bookstores"))
    
    translation_authors = models.ManyToManyField(
        Author, blank=True, related_name='books_translated', verbose_name=_("translation authors"))
    
    serie = models.ForeignKey(
        Serie, null=True, blank=True, related_name='books', verbose_name=_("serie"))
    
    form = models.ForeignKey(
        BookFormat, null=True, blank=True, related_name='books', verbose_name=_("format"))
    
    background_color = models.CharField(max_length=9, blank=True, verbose_name=_("background color"))
    
    file = models.FileField(blank=True, storage=storage_magazzino_virtuale)
    
    publication_date = models.DateTimeField(blank=True, null=True, verbose_name=_("publication date"))
    
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)
    
    # will be modified by signals on offer creation or deletion 
    has_offers = models.BooleanField(default=False) #noqa
    
    @property
    def digital_variants_aggregator(self):
        #check there is an ebook form variant on parent product
        p = self
        if self.is_child:
            p = self.parent
        return p.children.filter(form__slug='ebook').first()

    @property
    def aggregated_children(self):
        #return child proucts aggregated if there is the digital_variants_aggregator, all children andernfalls
        digital_variants_aggregator = self.digital_variants_aggregator
        p = self
        if self.is_child:
            p = self.parent
        if digital_variants_aggregator:
            return p.children.filter(Q(form__virtual=False) | Q(form__slug='ebook'))
        return p.children.all()
    
    @property
    def digital_children(self):
        #return child virtual proucts aggregated without aggregator
        p = self
        if self.is_child:
            p = self.parent
        return p.children.filter(Q(form__virtual=True) & ~Q(form__slug='ebook'))
        
            
    @property
    def is_on_sale(self):
        return self.has_offers
    
    @property
    def is_virtual(self):
        if self.form:
            return self.form.virtual
        return False

    @property
    def is_shipping_required(self):
        spedizione_richiesta = self.get_product_class().requires_shipping
        if self.is_virtual:
            return False
        return spedizione_richiesta
    
    @property
    def is_published(self):
        if self.publication_date:
            return timezone.now() >= self.publication_date
        return True
    
    @property
    def is_new(self):
        if self.is_published:
            if self.publication_date:
                return (self.publication_date + timedelta(getattr(settings, 'NEW_PRODUCT_DAYS', 30))) > timezone.now()
            return (self.date_created + timedelta(getattr(settings, 'NEW_PRODUCT_DAYS', 30))) > timezone.now()
        return False

    def primary_image(self):
        """
        Returns the primary image for a product. Usually used when one can
        only display one product image, e.g. in a list of products.
        """
        
        images = self.images.all()
        ordering = self.images.model.Meta.ordering
        if self.is_child:
            images = self.parent.images.all()
            ordering = self.parent.images.model.Meta.ordering
        
        
        if not ordering or ordering[0] != 'display_order':
            # Only apply order_by() if a custom model doesn't use default
            # ordering. Applying order_by() busts the prefetch cache of
            # the ProductManager
            images = images.order_by('display_order')
        try:
            return images[0]
        except IndexError:
            # We return a dict with fields that mirror the key properties of
            # the ProductImage class so this missing image can be used
            # interchangeably in templates.  Strategy pattern ftw!
            return {
                'original': self.get_missing_image(),
                'caption': '',
                'is_missing': True}


    def get_title(self):
        title = super(Product, self).get_title()
        
        if self.form:
            title += ' [{}]'.format(self.form.name)
        return title


from oscar.apps.catalogue.models import *  # noqa