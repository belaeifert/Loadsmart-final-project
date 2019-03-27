from django import forms

class LoadForm(forms.Form):
    pickup_date = forms.DateField(label='Pickup date')
    ref = forms.CharField(label='Ref')
    origin_city = forms.CharField(label='Origin City')
    destination_city = forms.CharField(label='Destination City')
    price = forms.FloatField(label='Price')

