from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from oscar.core.utils import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
import os

from oscar.core.loading import get_class, get_model

from apps.user.models import User

Order = get_model('order', 'Order')




@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(_('name'), max_length=128)
    description = models.TextField(_('description'), blank=True)
    
    slug = models.SlugField(_('slug'), max_length=128, unique=True, blank=True)
    image = models.ImageField(upload_to=os.path.join('images', 'series'), blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _('authors')

    def generate_slug(self):
        return slugify(self.name)
    
    def ensure_slug_uniqueness(self):
        unique_slug = self.slug
        siblings = Author.objects.exclude(id=self.id)
        next_num = 2
        while siblings.filter(slug=unique_slug).exists():
            unique_slug = '{slug}_{end}'.format(slug=self.slug, end=next_num)
            next_num += 1
        if unique_slug != self.slug:
            self.slug = unique_slug
            self.save()

    def save(self, *args, **kwargs):
        if self.slug and self.slug != '':
            self.ensure_slug_uniqueness()
            super(Author, self).save(*args, **kwargs)
        else:
            self.slug = self.generate_slug()
            self.ensure_slug_uniqueness()
            super(Author, self).save(*args, **kwargs)

    def num_books(self):
        return self.books.count()

    def num_translations(self):
        return self.books_translated.count()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})



@python_2_unicode_compatible
class Serie(models.Model):
    name = models.CharField(_('name'), max_length=128, unique=True)
    description = models.TextField(_('Description'), blank=True)
    
    slug = models.SlugField(_('slug'), max_length=128, unique=True, blank=True)
    
    image = models.ImageField(upload_to=os.path.join('images', 'series'), max_length=255,
        blank=True, null=True)
    
    background_color = models.CharField(max_length=9, blank=True, verbose_name=_("background color"))

    def generate_slug(self):
        return slugify(self.name)
    
    def ensure_slug_uniqueness(self):
        unique_slug = self.slug
        siblings = Serie.objects.exclude(id=self.id)
        next_num = 2
        while siblings.filter(slug=unique_slug).exists():
            unique_slug = '{slug}_{end}'.format(slug=self.slug, end=next_num)
            next_num += 1
        if unique_slug != self.slug:
            self.slug = unique_slug
            self.save()

    def save(self, *args, **kwargs):
        if self.slug and self.slug != '':
            self.ensure_slug_uniqueness()
            super(Serie, self).save(*args, **kwargs)
        else:
            self.slug = self.generate_slug()
            self.ensure_slug_uniqueness()
            super(Serie, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = _('series')

    def num_books(self):
        return self.books.count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('serie_detail', kwargs={'slug': self.slug})




@python_2_unicode_compatible
class BookFormat(models.Model):
    name = models.CharField(_('Name'), max_length=128, unique=True)
    description = models.TextField(_('Description'), blank=True)
    virtual = models.BooleanField(_('Virtual'), default=False)
    
    slug = models.SlugField(_('slug'), max_length=128, unique=True, blank=True)
    
    def generate_slug(self):
        return slugify(self.name)
    
    def ensure_slug_uniqueness(self):
        unique_slug = self.slug
        siblings = BookFormat.objects.exclude(id=self.id)
        next_num = 2
        while siblings.filter(slug=unique_slug).exists():
            unique_slug = '{slug}_{end}'.format(slug=self.slug, end=next_num)
            next_num += 1
        if unique_slug != self.slug:
            self.slug = unique_slug
            self.save()

    def save(self, *args, **kwargs):
        if self.slug and self.slug != '':
            self.ensure_slug_uniqueness()
            super(BookFormat, self).save(*args, **kwargs)
        else:
            self.slug = self.generate_slug()
            self.ensure_slug_uniqueness()
            super(BookFormat, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('book format')
        verbose_name_plural = _('book formats')
    
    def num_books(self):
        return self.books.count()
    
    def __str__(self):
        return self.name




@python_2_unicode_compatible
class BookStore(models.Model):
    name = models.CharField(_('Name'), max_length=128, unique=True)
    description = RichTextUploadingField()
    
    slug = models.SlugField(_('slug'), max_length=128, unique=True, blank=True)

    def generate_slug(self):
        return slugify(self.name)
    
    def ensure_slug_uniqueness(self):
        unique_slug = self.slug
        siblings = BookStore.objects.exclude(id=self.id)
        next_num = 2
        while siblings.filter(slug=unique_slug).exists():
            unique_slug = '{slug}_{end}'.format(slug=self.slug, end=next_num)
            next_num += 1
        if unique_slug != self.slug:
            self.slug = unique_slug
            self.save()

    def save(self, *args, **kwargs):
        if self.slug and self.slug != '':
            self.ensure_slug_uniqueness()
            super(BookStore, self).save(*args, **kwargs)
        else:
            self.slug = self.generate_slug()
            self.ensure_slug_uniqueness()
            super(BookStore, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name = _('book store')
        verbose_name_plural = _('book stores')
    
    def num_books(self):
        return self.books.count()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bookstore_detail', kwargs={'pk': self.pk})



@python_2_unicode_compatible
class DigitalDownload(models.Model):
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_('User'))
    product = models.ForeignKey('catalogue.Product', verbose_name=_('Product'))
    downloads_remaining = models.PositiveIntegerField(default=5)
    log = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _('Digital goods')
    
    def __str__(self):
        return '{0}, {1}'.format(self.user.email, self.order.number)

    def get_absolute_url(self):
        return reverse('digital_goods', kwargs={'id': self.id})

