from django.urls import path

from . import views

app_name = "carrier"

urlpatterns = [
    path('home/', views.CarrierHome.as_view(), name='home'),
    path('home/load/accept/<int:pk_load>/', views.AcceptLoad.as_view(), name='accept_load'),
    path('home/load/reject/<int:pk_load>/', views.RejectLoad.as_view(), name='reject_load'),
    path('home/load/drop/<int:pk_load>/', views.DropLoad.as_view(), name='drop_load'),
]
