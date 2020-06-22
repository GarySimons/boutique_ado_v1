from django import forms
from .models import Order

class OrderForm(forms.ModelForm)
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_addressw', 'street_address2', 
                  'town_or_city', 'postcode', 'country',
                  'county',)