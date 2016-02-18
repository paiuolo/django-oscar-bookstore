from django.test import TestCase

from apps.books.models import Author, BookStore, BookFormat, Serie

from oscar.core.utils import slugify
from oscar.core.loading import get_classes

Product, Category, ProductClass = get_classes('catalogue.models', ['Product', 'Category', 'ProductClass'])

from .test_utils import crea_modello

class ModelloNomeslugdescription():

    def puo_creare(self, Model):
        el1 = crea_modello(Model, name="Pippo", slug="pippo", description="bla")

        el_saved = Model.objects.first()
        self.assertEqual(el_saved, el1)

        elements = Model.objects.all()
        self.assertEqual(elements.count(), 1)

        self.assertEqual(elements[0].name, 'Pippo')
        self.assertEqual(elements[0].description, 'bla')
        self.assertEqual(elements[0].slug, 'pippo')


    def salvataggio_genera_slug(self, Model):
        el1 = crea_modello(Model, name="Piero")
        
        el_saved = Model.objects.filter(name='Piero')
        self.assertEqual(el_saved[0].slug, slugify(el1.name))

    def stesso_nome_slug_diversa(self, Model):
        el1 = crea_modello(Model, name="Piero")
        el2 = crea_modello(Model, name="Piero")
        
        el_saved = Model.objects.filter(name='Piero')
        #print('Slugs',el_saved[0].slug, el_saved[1].slug)
        self.assertNotEqual(el_saved[0].slug, el_saved[1].slug)
        
    def stesse_lettere_nome_slug_diversa(self, Model):
        el1 = crea_modello(Model, name = "Piero")
        el2 = crea_modello(Model, name = "piero")
        
        el_saved = Model.objects.filter(name__icontains='Piero')
        #print('Slugs',el_saved[0].slug, el_saved[1].slug)
        self.assertNotEqual(el_saved[0].slug, el_saved[1].slug)


class AuthorModelTest(ModelloNomeslugdescription, TestCase):
    def test_puo_creare_autori(self):
        self.puo_creare(Author)
        
    def test_salvataggio_autore_genera_slug(self):
        self.salvataggio_genera_slug(Author)

    def test_autori_stesso_nome_slug_diversa(self):
        self.stesso_nome_slug_diversa(Author)

    def test_get_absolute_url(self):
        el = Author.objects.create(name='Pippo')
        self.assertEqual(el.get_absolute_url(), '/books/authors/{}/'.format(el.slug))


class BookStoreModelTest(ModelloNomeslugdescription, TestCase):
    def test_puo_creare_bookstore(self):
        self.puo_creare(BookStore)
        
    def test_salvataggio_bookstore_genera_slug(self):
        self.salvataggio_genera_slug(BookStore)

    def test_bookstore_stesso_nome_slug_diversa(self):
        self.stesse_lettere_nome_slug_diversa(BookStore)

    def test_get_absolute_url(self):
        el = BookStore.objects.create(name='Pippo')
        self.assertEqual(el.get_absolute_url(), '/books/bookstores/{}/'.format(el.id))


class BookFormatModelTest(ModelloNomeslugdescription, TestCase):
    def test_puo_creare_bookformat(self):
        self.puo_creare(BookFormat)
        
    def test_salvataggio_bookformat_genera_slug(self):
        self.salvataggio_genera_slug(BookFormat)

    def test_bookformat_stesso_nome_slug_diversa(self):
        self.stesse_lettere_nome_slug_diversa(BookFormat)


class SerieModelTest(ModelloNomeslugdescription, TestCase):
    def test_puo_creare_serie(self):
        self.puo_creare(Serie)
        
    def test_salvataggio_serie_genera_slug(self):
        self.salvataggio_genera_slug(Serie)

    def test_serie_stesso_nome_slug_diversa(self):
        self.stesse_lettere_nome_slug_diversa(Serie)

    def test_get_absolute_url(self):
        el = Serie.objects.create(name='Serie1')
        self.assertEqual(el.get_absolute_url(), '/books/series/{}/'.format(el.slug))

    def test_serie_ha_immagine(self):
        image_field = Serie._meta.get_field('image')


class ProductModelTest(TestCase):
    def test_prodotto_tra_novità_i_primi_30_giorni(self):
        t = ProductClass.objects.create(name="Books")
        #c = Category.objects.create(name="cat1")
        p = Product.objects.create(title="Prod1", product_class=t)
        self.assertTrue(p.is_new)
        
    def test_prodotto_mostra_on_sale(self):
        t = ProductClass.objects.create(name="Books")
        el1 = crea_modello(Product, title="Prod1", product_class=t)
        
        self.assertFalse(el1.is_on_sale)
        
    def test_prodotto_ha_pagine_e_pubdate(self):
        t = ProductClass.objects.create(name="Books")
        el1 = crea_modello(Product, title="Prod1", product_class=t)
        
        self.assertIsNone(el1.publication_date)
        self.assertIsNone(el1.number_of_pages)
        



#from oscar.apps.catalogue.models import Product, ProductClass, ProductAttribute

#class ClassAttributesTest(TestCase):
    #def test_puo_associare_attributo_a_classe(self):
        #c = ProductClass()
        #c.name = 'Books'
        #c.track_stock = False
        #c.slug = 'books'
        #c.save()
        
        #a1 = Author.objects.create(name="Pippo")
        #a2 = Author.objects.create(name="Gianni")
        
        #al = AuthorList.objects.create()
        #al.authors.add(a1, a2)
        #al.save()
        
        #pa = ProductAttribute()
        #pa.product_class = c
        #pa.name = 'authors'
        #pa.code = 'authors'
        #pa.type = 'entity'
        #pa.save()
        
        #p = Product(product_class=c)
        #p.attr.authors = al
        #p.save()
        
        #pal = Product.objects.all()
        #print('Attributi prodotto', pal[0].attr.authors)
        
        
