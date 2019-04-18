from django.db import models
from finalProject.account.models import User
from finalProject.shipper.models import Load, ShipperUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class CarrierUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='carrier_user')
    MC_number = models.IntegerField(_('MC number'), null=False, blank=False)


class RejectedLoad(models.Model):
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    carrier = models.ForeignKey(CarrierUser, on_delete=models.CASCADE)
