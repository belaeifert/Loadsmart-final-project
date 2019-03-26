from django.db import models


class Carrier(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    MC_number = models.IntegerField()
    # password


class Load(models.Model):
    pickup_date = models.DateField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    price = models.FloatField()
    id_shipper = models.IntegerField()
    id_carrier = models.IntegerField(blank=True, null=True)
    #id_carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, blank=True, null=True)

