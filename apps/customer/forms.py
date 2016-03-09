from django import forms
from oscar.apps.customer.forms import UserForm
from oscar.core.compat import existing_user_fields, get_user_model

User = get_user_model()

class ProfileForm(UserForm):
    class Meta:
        model = User
        fields = existing_user_fields(['first_name', 'last_name', 'email', 'newsletter_subscribed']) 

