from django.urls import path
from finalProject.shipper import views

urlpatterns = [
    path('dashboard/', views.shipper_view)
]
