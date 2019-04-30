from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from . import views

app_name = "account"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-popup/', views.LogoutPopup, name='logout_popup'),
    path('redirect-home/', views.RedirectHome, name='redirect_home'),
    path('signup-shipper/', views.ShipperSignUpView.as_view(), name='shipper_signup'),
    path('signup-carrier/', views.CarrierSignUpView.as_view(), name='carrier_signup'),

    path('password/reset/',
         PasswordResetView.as_view(
             template_name='reset_password/password_reset_form.html',
             email_template_name='reset_password/reset_password_confirm.html',
             success_url=reverse_lazy('account:reset_password_done')
         ), name='reset_password'),
    path('password_reset_done',
         PasswordResetDoneView.as_view(
             template_name='reset_password/password_reset_done.html'
         ), name='reset_password_done'),

    path('password/reset/confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='reset_password/password_reset_confirm.html',
         ), name='reset_password_confirm'),

    path('password/reset/confirm/<uidb64>/<token>',
         PasswordResetCompleteView.as_view()),

]
