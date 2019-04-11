from django.contrib import admin
from .models import Carrier, Shipper, User

admin.site.register(Carrier)
admin.site.register(Shipper)
admin.site.register(User)
