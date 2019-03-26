from django.contrib import admin

# Register your models here.
from .models import Carrier, Load

admin.site.register(Carrier)
admin.site.register(Load)