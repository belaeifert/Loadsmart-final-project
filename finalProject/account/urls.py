from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/confirmation/', views.LogoutPopup, name='logout_popup'),
    path('redirect/home/', views.RedirectHome, name='redirect_home'),
    path('signup/shipper/', views.ShipperSignUpView.as_view(), name='shipper_signup'),
    path('signup/carrier/', views.CarrierSignUpView.as_view(), name='carrier_signup'),
    #path('password/reset/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    #path('password/reset/done/', views.CustomPasswordResetDoneView.as_view(), name='reset_password_done'),
    #path('password/reset/confirm/<uidb64>/<token>', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password/reset/complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
