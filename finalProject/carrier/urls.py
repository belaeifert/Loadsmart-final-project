from django.urls import path

from . import views

app_name = "carrier"

urlpatterns = [
    path('home/', views.listLoads, name='home'),
    path('home/load/accept/<int:pk_load>/', views.acceptLoad, name='accept_load'),
    path('home/load/reject/<int:pk_load>/', views.rejectLoad, name='reject_load'),
    path('home/load/drop/<int:pk_load>/', views.dropLoad, name='drop_load'),
]
