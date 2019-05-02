import datetime

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, TextInput

from finalProject.shipper.models import Load


def priceValidation(price):
    if price <= 0:
        raise forms.ValidationError("Price should be positive")
    if len(str(price).split('.')[1]) >= 3:
        raise forms.ValidationError("Price should have up to 2 decimal places")
    return price


class LoadForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    suggested_price = forms.FloatField(required=False, widget=forms.TextInput(
        attrs={'id': 'suggested_price_id', 'readonly': 'readonly'}))

    class Meta:
        model = Load
        fields = ['pickup_date', 'ref', 'origin_city',
                  'destination_city', 'price', 'suggested_price']
        widgets = {
            'pickup_date': DateInput(attrs={'type': 'date'}),
            'origin_city': TextInput(attrs={'id': 'origin_city_id'}),
            'destination_city': TextInput(attrs={'id': 'destination_city_id'}),
        }

    def clean_suggested_price(self):
        suggested_price = self.cleaned_data.get('suggested_price')
        if suggested_price is None or '':
            raise forms.ValidationError(
                "There are no road between origin and destination cities ")
        return suggested_price

    def clean_price(self):
        price = self.cleaned_data.get('price')
        return priceValidation(price)

    def clean_pickup_date(self):
        pickup_date = self.cleaned_data.get('pickup_date')
        if pickup_date < datetime.date.today():
            raise ValidationError('You can\'t use a past date for a new load.')
        return pickup_date


class UpdatePriceForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    suggested_price = forms.FloatField(required=False, disabled=True)
    ref = forms.CharField(required=False, disabled=True)

    class Meta:
        model = Load
        fields = ['ref', 'price', 'suggested_price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        return priceValidation(price)
