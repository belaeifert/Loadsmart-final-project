from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView


from finalProject.shipper.forms import LoadForm, UpdatePriceForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from finalProject.shipper.models import ShipperUser

from .models import Load

class ShipperView(LoginRequiredMixin, ListView):
    template_name = 'shipper_home.html'
    context_object_name = 'loads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key'] = settings.GOOGLE_API_KEY
        return context

    def get_queryset(self):
        shipper = ShipperUser.objects.get(user_id=self.request.user.id)
        return Load.objects.filter(shipper=shipper)


class PostLoadView(LoginRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'post_load.html'
    form_class = LoadForm
    success_message = 'Success: Load was posted.'
    success_url = reverse_lazy('shipper:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.shipper = ShipperUser.objects.get(user_id=self.request.user.id)
        super().form_valid(form)
        return redirect('shipper:home')


class EditPriceView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Load
    template_name = 'edit_price_modal.html'
    form_class = UpdatePriceForm
    success_message = 'Success: Load price was updated.'
    success_url = reverse_lazy('shipper:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        if obj.status == 'available':
            super().form_valid(form)
            return redirect('shipper:home')
        else:
            messages.error(self.request, 'ERROR: It is not possible to edit price because this load is not available anymore')
            return redirect('shipper:home')


class CancelLoadView(DeleteAjaxMixin, generic.DeleteView):
    model = Load
    template_name = 'cancel_load_modal.html'
    success_message = 'Success: Load was canceled.'
    success_url = '/shipper/home/'

    def delete(self, request, *args, **kwargs):
        try:
            super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, 'ERROR: This load is not available anymore')
            return redirect('/shipper/home/')



