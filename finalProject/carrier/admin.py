from django.contrib import admin
from .models import Carrier, Load, RejectedLoad


admin.site.register(Carrier)
admin.site.register(Load)
admin.site.register(RejectedLoad)