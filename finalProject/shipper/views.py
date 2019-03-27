from django.shortcuts import render

# Create your views here.
from finalProject.shipper.forms import LoadForm


def shipper_view(request):
    return render(request, 'dashboard.html', {'form':LoadForm()})

