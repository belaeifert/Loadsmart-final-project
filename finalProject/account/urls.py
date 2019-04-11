from django.urls import include, path
from . import views

app_name = "account"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('redirect-home/', views.RedirectHome, name='redirect_home'),
    path('signup/', views.SignUpView, name='signup'),
    path('signup/shipper/', views.ShipperSignUpView.as_view(), name='shipper_signup'),
    path('signup/carrier/', views.CarrierSignUpView.as_view(), name='carrier_signup'),
]