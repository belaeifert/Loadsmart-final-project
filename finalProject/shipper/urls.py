from django.urls import path
from finalProject.shipper.views import ShipperView, PostLoadView

app_name = "shipper"

urlpatterns = [
    path('home/', ShipperView.as_view(), name="home"),
    path('postLoad/', PostLoadView.as_view(), name="post_load"),
]
