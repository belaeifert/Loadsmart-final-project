from django.urls import path
from finalProject.shipper.views import ShipperView, PostLoadView, EditPriceView, CancelLoadView

app_name = "shipper"

urlpatterns = [
    path('home/', ShipperView.as_view(), name="home"),
    path('home/load/post/', PostLoadView.as_view(), name="post_load"),
    path('home/load/edit_price/<int:pk>', EditPriceView.as_view(), name='edit_price'),
    path('home/load/cancel/<int:pk>', CancelLoadView.as_view(), name='cancel_load'),
]
