from django.shortcuts import render, redirect
from .models import Load


def list_loads(request, pk_carrier):
    available_loads = Load.objects.filter(status='available')
    accepted_loads = Load.objects.filter(status='accepted', id_carrier=pk_carrier)
    return render(request, 'carrier_abas.html', {'available_loads': available_loads, 'accepted_loads': accepted_loads})


def accept_load(request, pk_load):
    load = Load.objects.get(pk=pk_load)
    load.status = 'accepted'
    #load.id_carrier = request.user.id
    load.id_carrier = 1
    load.save()
    return redirect('list_loads', pk_carrier=1)
    #return render(request, 'carrier_abas.html')
