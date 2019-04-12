from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Carrier, Shipper, User
from .forms import CarrierSignUpForm, ShipperSignUpForm


def RedirectHome(request):
    # After login, redirect Shipper/Carrier to respective homepage
    try:
        shipper = Shipper.objects.get(user__id=request.user.id)
        return redirect('shipper:dashboard')
    except:
        pass

    try:
        carrier = Carrier.objects.get(user__id=request.user.id)
        return redirect('carrier:list_loads', pk_carrier=request.user.id)
    except:
        pass


def SignUpView(request):
    return render(request, 'registration/signup.html')


class ShipperSignUpView(CreateView):
    model = Shipper
    form_class = ShipperSignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shipper:dashboard')


class CarrierSignUpView(CreateView):
    model = Carrier
    form_class = CarrierSignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('carrier:list_loads', pk_carrier=user.id)
