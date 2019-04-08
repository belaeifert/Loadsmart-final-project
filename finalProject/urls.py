from django.contrib import admin
from django.urls import path, include
from finalProject.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/', include('finalProject.api.urls')),
    path('carrier/', include('finalProject.carrier.urls')),
    path('shipper/', include('finalProject.shipper.urls'))
]
