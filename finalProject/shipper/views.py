from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from finalProject.shipper.forms import LoadForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from finalProject.shipper.models import ShipperUser


@login_required
def shipper_view(request):
    '''
    if request.method == 'POST':
        form = LoadForm(request.POST)
        if form.is_valid():
            Load.objects.create(**form.cleaned_data)
            messages.success(request, 'Successful Post!')
    '''
    context = {'form':LoadForm(), 'api_key': settings.GOOGLE_API_KEY}
    return render(request, 'dashboard.html', context)


class PostLoadView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'post-load.html'
    form_class = LoadForm
    success_message = 'Success: Load was posted.'
    success_url = reverse_lazy('shipper:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.shipper = ShipperUser.objects.get(user_id=self.request.user.id)
        super().form_valid(form)
        return redirect('shipper:home')



