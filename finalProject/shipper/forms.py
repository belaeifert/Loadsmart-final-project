from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from finalProject.shipper.models import Load


class LoadForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    pickup_date = forms.DateField(label='Pickup date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    ref = forms.CharField(label='Ref')
    origin_city = forms.CharField(label='Origin City', widget=forms.TextInput(attrs={'id':'origin_city_id', "class":"sourch_city"}))
    destination_city = forms.CharField(label='Destination City', widget=forms.TextInput(attrs={'id':'destination_city_id', "class":"sourch_city"}))
    price = forms.FloatField(label='Price')

    class Meta:
        model = Load
        fields = ['pickup_date', 'ref', 'origin_city', 'destination_city', 'price' ]

