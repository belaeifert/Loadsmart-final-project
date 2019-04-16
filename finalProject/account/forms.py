from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class ShipperSignUpForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    user_type = "Shipper" 

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        shipper = ShipperUser.objects.create(user=user)
        return user 


class CarrierSignUpForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm): 
    user_type = "Carrier" 

    mc_numb = forms.IntegerField(label='MC Number', required=True)

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name', 'mc_numb')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        carrier = CarrierUser.objects.create(
            user=user, MC_number=self.cleaned_data["mc_numb"])
        return user