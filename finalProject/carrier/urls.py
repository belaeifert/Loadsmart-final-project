from django.urls import path
from . import views


urlpatterns = [
    path('home/<int:pk_carrier>/', views.list_loads, name='list_loads'),
    path('home/accept_load/<int:pk_load>/', views.accept_load, name='accept_load'),
    path('home/reject_load/<int:pk_load>/', views.reject_load, name='reject_load'),
    path('home/drop_load/<int:pk_load>/', views.drop_load, name='drop_load'),
]