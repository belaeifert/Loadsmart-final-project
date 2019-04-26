from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


app_name = "account"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-popup/', views.LogoutPopup, name='logout_popup'),
    path('redirect-home/', views.RedirectHome, name='redirect_home'),
    path('signup-shipper/', views.ShipperSignUpView.as_view(), name='shipper_signup'),
    path('signup-carrier/', views.CarrierSignUpView.as_view(), name='carrier_signup'),
]