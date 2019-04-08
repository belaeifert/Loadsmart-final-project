from django.urls import path
from finalProject.shipper import views

app_name = "shipper"

urlpatterns = [
    path('dashboard/', views.shipper_view, name="dashboard"),
    path('postLoad/', views.PostLoadView.as_view(), name="post_load"),
]
