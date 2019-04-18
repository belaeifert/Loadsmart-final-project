from django.db import models
from finalProject.account.models import User


class ShipperUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='shipper_user')

    def __repr__(self):
        return "ID: {}, Name: {}".format(self.pk, self.user.first_name)


class Load(models.Model):
    pickup_date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=500, blank=True)
    destination_city = models.CharField(max_length=500, blank=True)
    price = models.FloatField()
    status = models.CharField(max_length=50)
    suggested_price = models.FloatField(null=True)
    carrier = models.ForeignKey('carrier.CarrierUser', on_delete=models.CASCADE, blank=True, null=True)
    shipper = models.ForeignKey(ShipperUser, on_delete=models.CASCADE, blank=True)

    def __repr__(self):
        return "Pickup date: {}, REF: {}, Origin City: {}, Destination city: {}, Price: {}".format(
            self.pickup_date, self.ref, self.origin_city, self.destination_city, self.price)

    def carrier_price(self):
        return self.price*0.95

