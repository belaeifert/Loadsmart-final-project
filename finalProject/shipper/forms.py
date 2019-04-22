from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.forms import DateInput, TextInput

from finalProject.shipper.models import Load, ShipperUser


class LoadForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    '''
    pickup_date = forms.DateField(label='Pickup date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    ref = forms.CharField(label='Ref')
    origin_city = forms.CharField(label='Origin City', widget=forms.TextInput(attrs={'id':'origin_city_id'}))
    destination_city = forms.CharField(label='Destination City', widget=forms.TextInput(attrs={'id':'destination_city_id'}))
    price = forms.FloatField(label='Price')
    suggested_price = forms.FloatField(label='Suggested price', disabled=True, required=False, widget=forms.TextInput(attrs={'id':'suggested_price_id'}))
'''

    class Meta:
        model = Load
        fields = ['pickup_date', 'ref', 'origin_city', 'destination_city', 'price', 'suggested_price']
        widgets = {
            'pickup_date': DateInput(attrs={'type': 'date'}),
            'origin_city': TextInput(attrs={'id': 'origin_city_id'}),
            'destination_city': TextInput(attrs={'id': 'destination_city_id'}),
            'suggested_price': TextInput(attrs={'id': 'suggested_price_id'}),
        }

    def clean_suggested_price(self, *args, **kwargs):
        suggested_price = self.cleaned_data.get('suggested_price')
        if suggested_price is None or '':
            raise forms.ValidationError("There are no road between origin and destination cities ")
        return suggested_price

