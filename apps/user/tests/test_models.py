from django.test import TestCase


from apps.user.models import User

class UserModelTest(TestCase):
    def test_ha_campo_newsletter_subscription(self):
        u = User.objects.create(email='user@example.com')
        
        _u = User.objects.get(email='user@example.com')
        
        self.assertTrue(_u.newsletter_subscribed)
