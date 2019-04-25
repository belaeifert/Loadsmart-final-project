from django.contrib import admin
from .models import ShipperUser, Load


class LoadModelAdmin(admin.ModelAdmin):
    list_display = ('ref', 'origin_city', 'destination_city', 'price', 'status')



admin.site.register(ShipperUser)
admin.site.register(Load, LoadModelAdmin)
