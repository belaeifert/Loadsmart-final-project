from django.db import models
from finalProject.account.models import User
from datetime import date


class ShipperUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='shipper_user')

    class Meta:
        verbose_name = 'Shipper'
        verbose_name_plural = 'Shippers'

    def __str__(self):
        return "shipper id: {}, user id: {}, Name: {}".format(
            self.pk, self.user.pk, self.user.first_name
        )

    #def __repr__(self):
    #    return "ID: {}, Name: {}".format(self.pk, self.user.first_name)

    #def __str__(self):
    #    return self.user.first_name + ' ' + self.user.last_name


class Load(models.Model):
    pickup_date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=500)
    destination_city = models.CharField(max_length=500)
    price = models.FloatField()
    status = models.CharField(max_length=50, default="available")
    suggested_price = models.FloatField(null=True)
    carrier = models.ForeignKey('carrier.CarrierUser', on_delete=models.CASCADE, blank=True, null=True)
    shipper = models.ForeignKey(ShipperUser, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Load'
        verbose_name_plural = 'Loads'

    def accept_load(self, carrier):
        self.status = 'accepted'
        self.carrier = carrier
        self.save()

    def drop_load(self):
        self.status = 'available'
        self.carrier = None
        self.save()

    def carrier_price(self):
        return round(self.price*0.95, 2)

    def delete(self, using=None, keep_parents=False):
        if (self.pickup_date <= date.today()) and (self.status == 'accepted'):
            raise Exception('The load was already picked up')
        super(Load, self)

    def __str__(self):
        return "Pickup date: {}, REF: {}, Origin City: {}, Destination city: {}, Price: {}, Carrier: {}, Shipper: {}".format(
            self.pickup_date, self.ref, self.origin_city, self.destination_city,
            self.price, self.carrier, self.shipper)

    #def __str__(self):
    #    return self.ref
    