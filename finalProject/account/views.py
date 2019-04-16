from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser
from .forms import CarrierSignUpForm, ShipperSignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import LoginAjaxMixin, PassRequestMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('account:redirect_home')


def RedirectHome(request):
    # After login, redirect Shipper/Carrier to respective homepage
    try:
        shipper = ShipperUser.objects.get(user__id=request.user.id)
        return redirect('shipper:home')
    except:
        pass
    try:
        carrier = CarrierUser.objects.get(user__id=request.user.id)
        return redirect('carrier:list_loads')
    except:
        pass


class ShipperSignUpView(PassRequestMixin, SuccessMessageMixin, CreateView):
    model = ShipperUser
    form_class = ShipperSignUpForm
    template_name = 'registration/signup_form.html'
    success_message = 'Success: Sign up succeeded.'

    def form_valid(self, form):
        if not self.request.is_ajax():
            user = form.save()
            login(self.request, user)
            #messages.success(self.request, self.success_message)
        return redirect('shipper:home')


class CarrierSignUpView(PassRequestMixin, SuccessMessageMixin, CreateView):
    model = CarrierUser
    form_class = CarrierSignUpForm
    template_name = 'registration/signup_form.html'
    success_message = 'Success: Sign up succeeded.'

    def form_valid(self, form):
        if not self.request.is_ajax():
            user = form.save()
            login(self.request, user)
            #messages.success(self.request, self.success_message)
        return redirect('carrier:list_loads')

