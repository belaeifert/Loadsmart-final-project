from django.db import models

class Carrier(models.Model):
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    mc_number = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    #password


class Shipper(models.Model):
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    #password


class Load(models.Model):
    #pickup_date = models.DateTimeField()
    ref = models.CharField(max_length=50) # which pattern
    origin_city = models.CharField(max_length=500, blank=True)
    destination_city = models.CharField(max_length=500, blank=True)
    price = models.FloatField()
    #suggested_price = models.FloatField(blank=True)
    #carrier = models.ForeignKey(Carrier, blank=True, on_delete=models.CASCADE)
    #shipper = models.ForeignKey(Shipper, blank=True, on_delete=models.CASCADE) #blank=False