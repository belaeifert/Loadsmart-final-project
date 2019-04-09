from django.contrib import admin
from django.urls import path, include
from finalProject.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('api/', include('finalProject.api.urls'), name="api"),
    path('carrier/', include('finalProject.carrier.urls'), name='carrier'),
    path('shipper/', include('finalProject.shipper.urls'), name='shipper')
]
