from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape

from apps.books.views import AuthorDetail, AuthorList

from oscar.core.loading import get_class

from django.contrib.auth.models import User

from decimal import Decimal as D

Selector = get_class('partner.strategy', ('Selector'))
Basket = get_class('basket.models', 'Basket')
Product = get_class('catalogue.models', 'Product')
ProductClass = get_class('catalogue.models', 'ProductClass')
ProductCategory = get_class('catalogue.models', 'ProductCategory')
Country = get_class('address.models', 'Country')
Repository = get_class('shipping.repository', ('Repository'))
OrderCreator = get_class('order.utils', 'OrderCreator')
OrderTotalCalculator = get_class('checkout.calculators', 'OrderTotalCalculator')
Partner = get_class('partner.models', 'Partner')
StockRecord = get_class('partner.models', 'StockRecord')


from django.conf import settings
from apps.books.models import Author, Serie, BookFormat
import os
from django.core.files.uploadedfile import SimpleUploadedFile

from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import timedelta

from .test_utils import crea_modello


class ImageModelTest():

    def setUp(self):
        self.test_image = SimpleUploadedFile(name=settings.OSCAR_MISSING_IMAGE_URL, content=open(os.path.join(settings.MEDIA_ROOT, settings.OSCAR_MISSING_IMAGE_URL), 'rb').read(), content_type='image/jpeg')
    def tearDown(self):
        for el in self.model.objects.all():
            if el.image:
                #print('Immagine rimasta', el, el.image, el.image.path)
                os.remove( el.image.path )
                
    def test_detail_mostra_immagine(self):
        el1 = crea_modello(self.model, name="{}_1".format(self.model.__name__), image=self.test_image)
        response = self.client.get(el1.get_absolute_url())
        self.assertEqual(response.context['object'].image, el1.image)




# User views
class AuthorTest(ImageModelTest, TestCase):
    
    model = Author
    
    def test_list_usa_giusto_template(self):
        el1 = crea_modello(Author, name='Arg1')
        response = self.client.get('/books/authors/')
        self.assertTemplateUsed(response, 'books/author_list.html')
    
    def test_detail_usa_giusto_template(self):
        el1 = crea_modello(Author, name='Arg1')
        el1_url = el1.get_absolute_url()
        response = self.client.get(el1_url)
        self.assertTemplateUsed(response, 'books/author_detail.html')
        
        
class SerieTest(ImageModelTest, TestCase):
    
    model = Serie
    
    def test_list_usa_giusto_template(self):
        el1 = crea_modello(Serie, name='Arg1')
        response = self.client.get('/books/series/')
        self.assertTemplateUsed(response, 'books/serie_list.html')
    
    def test_detail_usa_giusto_template(self):
        el1 = crea_modello(Serie, name='Arg1')
        el1_url = el1.get_absolute_url()
        response = self.client.get(el1_url)
        self.assertTemplateUsed(response, 'books/serie_detail.html')
    




class ProductTest(TestCase):
    fixtures = ['test_models.json']
    
    @classmethod
    def setUpTestData(cls):
        cls.product_class = ProductClass.objects.get(name="Book")
    
    def test_product_detail_does_not_show_price_before_pubdate(self):
        p = crea_modello(Product, title="Prod1", product_class=self.product_class, publication_date=timezone.now())
        response = self.client.get(p.get_absolute_url())
        self.assertNotContains(response, 'variazione_prodotto')
        
    def test_product_detail_show_pubdate_before_pubdate(self):
        p = crea_modello(Product, title="Prod1", product_class=self.product_class, publication_date=timezone.now()+timedelta(30))
        response = self.client.get(p.get_absolute_url())
        self.assertContains(response, 'data_pubblicazione_prodotto')
        
    def test_product_detail_shows_one_digital_variants_button_if_ebook_variant_specified(self):
        p = Product.objects.get(title='Libro 2')
        response = self.client.get(p.get_absolute_url())
        contenuto = str(response.content)
        num_butt = contenuto.count('variazione_prodotto')
        self.assertEqual(num_butt, len(p.aggregated_children))

    def test_product_detail_shows_all_digital_variants_button_if_ebook_variant_not_specified(self):
        p = Product.objects.get(title='Libro 1')
        response = self.client.get(p.get_absolute_url())
        contenuto = str(response.content)
        num_butt = contenuto.count('variazione_prodotto')
        self.assertEqual(num_butt, len(p.aggregated_children))


"""


# Dashboard views
class SerieDashboardTest(TestCase):
    def test_vista_update_mostra_campo_image(self):
        s = crea_modello(Serie, name="Serie1")
        #!!da finire
        print('modello serie', s)




def crea_ordine():

    p_cl = ProductClass.objects.create(name='Books', track_stock=False)
    
    p = Product.objects.create(title='prodotto1', product_class=p_cl)
    
    partner = Partner.objects.create(name='partner1')

    stock = StockRecord.objects.create( product=p, partner=partner, price_excl_tax=D(10), num_in_stock=1)

    b=Basket()

    user=User.objects.all()[0]

    b.strategy=Selector().strategy()
    
    b.add_product(product=p,quantity=1)
    
    nazione = Country.objects.all()[0]
    
    shipping_address = None
    
    shipping_method = Repository().get_default_shipping_method(basket=b, shipping_address=shipping_address)
    shipping_charge = shipping_method.calculate(b)
    order_total = OrderTotalCalculator().calculate(b, shipping_charge)
    b.submit()
    o=OrderCreator().place_order(b,order_total,shipping_method,shipping_charge,user,shipping_address)
    print("ordine", o, "basket", b, "pipeline", o.pipeline, "user", o.user)
    return o

class SendOrderToEmailViewTest(TestCase):
    fixtures = ['admin_user.json', 'address.country.json']
    
    def test_url(self):
        
        #L'url radice punta alla vista?
        
        o = crea_ordine()
        vista = SendOrderToEmailView
        trovata = resolve('/accounts/orders/{}/resend/'.format(o.number))
        self.assertEqual(trovata.func, vista.as_view())

"""

"""
class AuthorListTest(TestCase):
    def test_usa_giusto_template(self):
        el1 = Author.objects.create(titolo='Arg1')
        response = self.client.get('/books/authors/{}/'.format(arg1.id))
        self.assertTemplateUsed(response, 'author_list.html')


    def test_mostra_solo_le_sue_pubblicazioni(self):
        arg1 = Argomento.objects.create(titolo='Arg1')
        arg2 = Argomento.objects.create(titolo='Arg2')

        pub1 = Pubblicazione.objects.create(testo='Prima', argomento=arg1)
        pub2 = Pubblicazione.objects.create(testo='Seconda', argomento=arg1)
        pub3 = Pubblicazione.objects.create(testo='Terza', argomento=arg2)

        response = self.client.get('/argomenti/{}/'.format(arg1.id))

        self.assertContains(response, pub1.testo)
        self.assertContains(response, pub2.testo)
        self.assertNotContains(response, pub3.testo)

    def test_torna_argomento_selezionato(self):
        arg1 = Argomento.objects.create(titolo='Arg1')
        response = self.client.get('/argomenti/{}/'.format(arg1.id))
        self.assertEqual(response.context['argomento_selezionato'], arg1)

    def test_redirect_dopo_POST_crea_pubblicazione(self):
        arg1 = Argomento.objects.create(titolo='Arg1')
        response = self.client.post(
                '/argomenti/{}/add_pubblicazione'.format(arg1.id),
                {
                'testo_nuova_pubblicazione': 'Pubblicazione 1.',
                }
           )
        self.assertRedirects(response, '/argomenti/{}/'.format(arg1.id))

    def test_puo_creare_pubblicazioni(self):
        arg1 = Argomento.objects.create(titolo='Arg1')
        response = self.client.post(
                '/argomenti/{}/add_pubblicazione'.format(arg1.id),
                {
                'testo_nuova_pubblicazione': 'Pubblicazione 1.',
                }
            )
        pubblicazioni_argomento = Pubblicazione.objects.filter(argomento=arg1)
        self.assertEqual(pubblicazioni_argomento.count(), 1)
        self.assertEqual(pubblicazioni_argomento[0].testo, 'Pubblicazione 1.')





class CreaArgomentoTest(TestCase):
    def test_crea_argomento_salva_POST(self):
        self.client.post(
                '/argomenti/new',
                data={'titolo_nuovo_argomento':'Arg1'}
            )
        self.assertEqual(Argomento.objects.count(), 1)
        nuovo_argomento = Argomento.objects.first()
        self.assertEqual(nuovo_argomento.titolo, 'Arg1')

    def test_crea_argomento_reindirizza_dopo_POST(self):
        response = self.client.post(
                '/argomenti/new',
                data={'titolo_nuovo_argomento':'Arg1'}
            )
        nuovo_argomento = Argomento.objects.first()
        self.assertRedirects(response, '/argomenti/{}/'.format(nuovo_argomento.id))

    def test_rimanda_a_home_se_trova_errori_di_validazione(self):
        response = self.client.post(
                '/argomenti/new',
                data = {'titolo_nuovo_argomento': ''}
                )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        testo_errore = escape("Il titolo dell'argomento non può essere vuoto")
        self.assertContains(response, testo_errore)
    
    def test_non_salva_argomenti_con_titolo_vuoto(self):
        self.client.post('/argomenti/new', data={'testo_nuovo_argomento': ''})
        self.assertEqual(Argomento.objects.count(), 0)

"""