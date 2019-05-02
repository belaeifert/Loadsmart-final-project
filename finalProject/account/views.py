from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser
from .forms import CarrierSignUpForm, ShipperSignUpForm

from bootstrap_modal_forms.mixins import LoginAjaxMixin, PassRequestMixin


class CustomLoginView(LoginAjaxMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = 'registration/login.html'
    success_message = None
    redirect_authenticated_user = True


def LogoutPopup(request):
    return render(request, 'registration/logout_modal.html')


def RedirectHome(request):
    # After login, redirect Shipper/Carrier to respective homepage
    try:
        ShipperUser.objects.get(user__id=request.user.id)
        return redirect('shipper:home')
    except:
        try:
            CarrierUser.objects.get(user__id=request.user.id)
            return redirect('carrier:home')
        except:
            return redirect('index')


class ShipperSignUpView(PassRequestMixin, CreateView):
    model = ShipperUser
    form_class = ShipperSignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        if not self.request.is_ajax():
            user = form.save()
            login(self.request, user)
        return redirect('shipper:home')


class CarrierSignUpView(PassRequestMixin, CreateView):
    model = CarrierUser
    form_class = CarrierSignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        if not self.request.is_ajax():
            user = form.save()
            login(self.request, user)
        return redirect('carrier:home')

'''
class CustomPasswordResetView(PasswordResetView):
    template_name='reset_password/password_reset_form.html'
    email_template_name='reset_password/password_reset_email.html'
    subject_template_name='reset_password/password_reset_subject.txt'
    success_url=reverse_lazy('account:reset_password_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name='reset_password/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='reset_password/password_reset_confirm.html'
    success_url=reverse_lazy('account:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='reset_password/password_reset_complete.html'
'''