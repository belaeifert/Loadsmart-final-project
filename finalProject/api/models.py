from django.db import models

# After we have to reorganized this class to app load
class Load(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    price = models.FloatField()
