from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GenericTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1280, 800)
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()
        
    def corpo_contiene_testo(self, testo):
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(testo, body.text)
        
    def corpo_non_contiene_testo(self, testo):
        body = self.browser.find_element_by_tag_name('body')
        self.assertNotIn(testo, body.text)        

class AdminsTest(GenericTest):
    fixtures = ['user.json',
                'catalogue.json']
        
    def test_puo_creare_un_prodotto(self):
        # Si connette all'interfaccia di amministrazione
        self.browser.get(self.live_server_url + '/dashboard/')

        # Riconosce l'interfaccia
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Log In', body.text)

        # Inserisce i dati di accesso
        username_field = self.browser.find_element_by_name('login-username')
        username_field.send_keys('paiuolo@gmail.com')

        password_field = self.browser.find_element_by_name('login-password')
        password_field.send_keys('supercacca')
        password_field.send_keys(Keys.RETURN)

        # Confermati i dati di accesso viene rediretta alla pagina dashboard
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Dashboard', body.text)

        # Cerca tra le voci nel menu su quella catalogo
        catalogue_links = self.browser.find_elements_by_link_text('Catalogue')
        self.assertEquals(len(catalogue_links), 1)
        
        # Clicca sulla voce catalogo, vede il link ai prodotti e ci clicca
        catalogue_links[0].click()
        goto_create_product_link = self.browser.find_element_by_link_text('Products')
        goto_create_product_link.click()
        
        # Viene reindirizzato alla pagina di creazione articoli
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Products', body.text)
        
        #Preme sul tasto nuovo articolo
        create_product_button = self.browser.find_element_by_xpath("//button[contains(.,'New Product')]")
        create_product_button.click()
        
        #Viene reindirizzato alla pagina di creazione articolo
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Create new Books product', body.text)
        
        #inserisce il nome dell'articolo
        product_title_input = self.browser.find_element_by_id("id_title")
        product_title_input.send_keys("Prodotto1")
        
        #assegna una categoria
        product_category_selector = self.browser.find_element_by_xpath('//a[@href="#product_category"]')
        product_category_selector.click()
        product_category_choose = self.browser.find_element_by_id("select2-chosen-5")
        product_category_choose.click()
        product_category_input = self.browser.find_element_by_id("s2id_autogen5_search")
        product_category_input.send_keys('books')
        product_category_input.send_keys(Keys.RETURN)        
        
        #salva il prodotto e continua le modifiche
        save_and_continue_button = self.browser.find_element_by_xpath('//button[@name="action" and @value="continue"]')
        save_and_continue_button.click()
    
        #viene caricata la pagina di modifica
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Prodotto1', body.text)



        
        # TODO: Gertrude uses the admin site to create a
        #self.fail('todo: finire test')


class UsersTest(GenericTest):
    
    def test_puo_registrarsi(self):
        # Gaia accede al sito
        self.browser.get(self.live_server_url)
        
        # Nota l'eleganza della pagina e decide di registrarsi. Per fare cio preme sul pulsante accedi o registrati
        login_link = self.browser.find_element_by_id("login_link")
        login_link.click()
    
        # riconosce il form di registrazione
        self.corpo_contiene_testo('register')
        
        # lo compila
        email_input = self.browser.find_element_by_id('id_registration-email')
        password_input1 = self.browser.find_element_by_id('id_registration-password1')
        password_input2 = self.browser.find_element_by_id('id_registration-password2')

        email_input.send_keys('gaia@example.com')
        password_input1.send_keys('09876543210abcde')
        password_input2.send_keys('09876543210abcde')
        password_input2.send_keys(Keys.RETURN)
    
        #inviato il form viene reindirizzata alla pagina principale e legge il messaggio di benvenuto
        self.corpo_contiene_testo('Thanks for registering!')

        # decide di de-registrarsi dalla newsletter, per fare cio entra nella sezione profilo cliccando sul pulsante
        tasto_profilo = self.browser.find_element_by_xpath('//a[@href="/accounts/"]')
        tasto_profilo.click()
        
        #viene reindirizzata alla pagina profilo dove trova il tasto per modificarlo e lo preme
        self.corpo_contiene_testo('profile')
        tasto_modifica_profilo = self.browser.find_element_by_xpath('//a[@href="/accounts/profile/edit/"]')
        tasto_modifica_profilo.click()
        
        #trova la checkbox del campo newsletter_subscribed e la spunta
        checkbox_newsletter = self.browser.find_element_by_id('id_newsletter_subscribed')
        checkbox_newsletter.click()
        
        #preme il pulsante di salvataggio
        save_button = self.browser.find_element_by_xpath("//button[contains(.,'Save')]")
        save_button.click()
        
        #time.sleep(5)
        #vede che il campo è impostato a -
        self.corpo_non_contiene_testo('True')
        
        print('\n Fine test Utente')
        #time.sleep(10)
    
    

"""
    def test_can_create_new_poll_via_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # She types in her username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('paiuolo@gmail.com')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('supercacca')
        password_field.send_keys(Keys.RETURN)

        # her username and password are accepted, and she is taken to
        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # She now sees a couple of hyperlink that says "Polls"
        authors_links = self.browser.find_elements_by_link_text('Authors')
        self.assertEquals(len(authors_links), 1)
        
        # TODO: Gertrude uses the admin site to create a new Author
        self.fail('todo: finish tests')
"""        
