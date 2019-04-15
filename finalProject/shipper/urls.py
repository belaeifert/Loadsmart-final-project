from django.urls import path
from finalProject.shipper import views

app_name = "shipper"

urlpatterns = [
    path('home/', views.shipper_view, name="home"),
    path('postLoad/', views.PostLoadView.as_view(), name="post_load"),
]
