from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from django.db import transaction
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from finalProject.carrier.models import RejectedLoad, CarrierUser
from finalProject.shipper.models import Load
from finalProject.settings import DEFAULT_FROM_EMAIL


class CarrierHome(LoginRequiredMixin, ListView):
    template_name = 'carrier_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_loads'] = self.available_loads
        context['accepted_loads'] = self.accepted_loads
        context['rejected_loads'] = self.rejected_loads
        return context

    def get_queryset(self):
        carrier = CarrierUser.objects.get(user_id=self.request.user.id)
        rej_loads = RejectedLoad.objects.filter(carrier=carrier)
        self.available_loads = Load.objects.filter(status='available').exclude(
            id__in=rej_loads.values('load_id'))
        self.accepted_loads = Load.objects.filter(
            status='accepted', carrier=carrier)
        self.rejected_loads = Load.objects.filter(id__in=rej_loads.values('load_id'))


class AcceptLoad(LoginRequiredMixin, UpdateView):
    model = Load
    template_name = 'carrier_home.html'
    success_url = reverse_lazy('carrier:home')

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        try:
            load = Load.objects.get(pk=kwargs['pk_load'], status='available')
        except:
            messages.error(request, 'ERROR: This load is not available anymore')
            return redirect('carrier:home')

        carrier = CarrierUser.objects.get(user_id=request.user.id)
        load.accept_load(carrier)
        messages.success(request, 'Load accepted successfully')
        '''
        email_subject = 'Your load was accepted'
        html_message = render_to_string('email_message_load_accepted.html', {'load': load})
        from_email = DEFAULT_FROM_EMAIL
        to_email = [load.shipper.user.email]
        send_mail(email_subject, html_message, from_email, to_email)
        '''
        return redirect('carrier:home')


class RejectLoad(LoginRequiredMixin, UpdateView):
    model = Load
    template_name = 'carrier_home.html'
    success_url = reverse_lazy('carrier:home')

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        try:
            load = Load.objects.get(pk=kwargs['pk_load'], status='available')
        except:
            messages.error(request, 'ERROR: This load is not available anymore')
            return redirect('carrier:home')

        carrier = CarrierUser.objects.get(user_id=request.user.id)
        RejectedLoad.objects.create(load=load, carrier=carrier)
        messages.success(request, 'Load rejected successfully')
        return redirect('carrier:home')


class DropLoad(LoginRequiredMixin, UpdateView):
    model = Load
    template_name = 'carrier_home.html'
    success_url = reverse_lazy('carrier:home')

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        try:
            carrier = CarrierUser.objects.get(user_id=request.user.id)
            load = Load.objects.get(pk=kwargs['pk_load'], status='accepted', carrier=carrier)
        except:
            messages.error(request, 'ERROR: This load is not accepted by you')
            return redirect('carrier:home')

        load.drop_load()
        RejectedLoad.objects.create(load=load, carrier=carrier)
        messages.success(request, 'Load dropped successfully')
        '''
        email_subject = 'Your load was dropped'
        html_message = render_to_string('email_message_load_dropped.html', {'load': load})
        from_email = DEFAULT_FROM_EMAIL
        to_email = [load.shipper.user.email]
        send_mail(email_subject, html_message, from_email, to_email)
        '''
        return redirect('carrier:home')
