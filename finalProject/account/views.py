from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser
from .forms import CarrierSignUpForm, ShipperSignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from bootstrap_modal_forms.mixins import LoginAjaxMixin, PassRequestMixin


class CustomLoginView(LoginAjaxMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = 'registration/login.html'
    success_message = None
    redirect_authenticated_user = True


def LogoutPopup(request):
    return render(request,'registration/logout_modal.html')


def RedirectHome(request):
    # After login, redirect Shipper/Carrier to respective homepage
    try:
        shipper = ShipperUser.objects.get(user__id=request.user.id)
        return redirect('shipper:home')
    except:
        try:
            carrier = CarrierUser.objects.get(user__id=request.user.id)
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

