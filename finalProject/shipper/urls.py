from django.urls import path
from finalProject.shipper.views import ShipperView, PostLoadView, EditPriceView, CancelLoadView

app_name = "shipper"

urlpatterns = [
    path('home/', ShipperView.as_view(), name="home"),
    path('postLoad/', PostLoadView.as_view(), name="post_load"),
    path('editPrice/<int:pk>', EditPriceView.as_view(), name='edit_price'),
    path('cancelLoad/<int:pk>', CancelLoadView.as_view(), name='cancel_load'),
]
