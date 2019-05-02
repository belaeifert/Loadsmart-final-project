from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.core.mail import send_mail
from django.template.loader import render_to_string

from finalProject.shipper.forms import LoadForm, UpdatePriceForm
from finalProject.shipper.models import ShipperUser
from .models import Load
from finalProject.settings import DEFAULT_FROM_EMAIL


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
            messages.error(self.request,
                           'ERROR: It is not possible to edit price because this load is not available anymore')
            return redirect('shipper:home')


class CancelLoadView(DeleteAjaxMixin, generic.DeleteView):
    model = Load
    template_name = 'cancel_load_modal.html'
    success_message = 'Success: Load was canceled.'
    success_url = '/shipper/home/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        '''
        if self.object.status == 'accepted':
            load = self.object
            email_subject = 'Shipper canceled an accepted load'
            html_message = render_to_string('email_message_load_canceled.html', {'load': load})
            from_email = DEFAULT_FROM_EMAIL
            to_email = [load.carrier.user.email]
            send_mail(email_subject, html_message, from_email, to_email)
        '''
        return self.delete(request, *args, **kwargs)
