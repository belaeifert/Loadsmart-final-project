from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from finalProject.shipper.models import Load


class LoadForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    pickup_date = forms.DateField(label='Pickup date', widget=forms.SelectDateWidget())
    ref = forms.CharField(label='Ref')
    origin_city = forms.CharField(label='Origin City')
    destination_city = forms.CharField(label='Destination City')
    price = forms.FloatField(label='Price')

    class Meta:
        model = Load
        fields = ['ref', 'origin_city', 'destination_city', 'price' ]

