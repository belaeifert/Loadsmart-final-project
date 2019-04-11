from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Shipper, Carrier, User


class CustomCarrierCreationForm(UserCreationForm):
    mc_numb = forms.IntegerField(label='MC Number', required=True)

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name', 'mc_numb')


class CustomShipperCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name')


class CarrierSignUpForm(CustomCarrierCreationForm):

    class Meta(CustomCarrierCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        carrier = Carrier.objects.create(
            user=user, MC_number=self.cleaned_data["mc_numb"])
        return user


class ShipperSignUpForm(CustomShipperCreationForm):

    class Meta(CustomShipperCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        shipper = Shipper.objects.create(user=user)
        return user
