from django.db import models

class Shipper(models.Model):
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    #password


class Load(models.Model):
    pickup_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=50) # which pattern
    origin_city = models.CharField(max_length=500, blank=True)
    destination_city = models.CharField(max_length=500, blank=True)
    price = models.FloatField()
    #suggested_price = models.FloatField(blank=True)
    #carrier = models.ForeignKey(Carrier, blank=True, on_delete=models.CASCADE)
    #shipper = models.ForeignKey(Shipper, blank=True, on_delete=models.CASCADE) #blank=False

    def __repr__(self):
        return "Pickup date: {}, REF: {}, Origin City: {}, Destination city: {}, Price: {}".format(
            self.pickup_date, self.ref, self.origin_city, self.destination_city, self.price)
