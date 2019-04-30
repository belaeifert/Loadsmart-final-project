from django.urls import path
from . import views

app_name = "carrier"

urlpatterns = [
    path('home/', views.list_loads, name='home'),
    path('home/load/accept/<int:pk_load>/', views.accept_load, name='accept_load'),
    path('home/load/reject/<int:pk_load>/', views.reject_load, name='reject_load'),
    path('home/load/drop/<int:pk_load>/', views.drop_load, name='drop_load'),
]