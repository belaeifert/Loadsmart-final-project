from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from finalProject.carrier.models import RejectedLoad, CarrierUser
from finalProject.shipper.models import Load


@login_required
def listLoads(request):
    carrier = CarrierUser.objects.get(user_id=request.user.id)

    rej_loads = RejectedLoad.objects.filter(carrier=carrier)
    available_loads = Load.objects.filter(status='available').exclude(
        id__in=rej_loads.values('load_id'))
    accepted_loads = Load.objects.filter(
        status='accepted', carrier=carrier)
    rejected_loads = Load.objects.filter(id__in=rej_loads.values('load_id'))

    return render(request, 'carrier_home.html', {
        'available_loads': available_loads,
        'accepted_loads': accepted_loads,
        'rejected_loads': rejected_loads})


@login_required
@transaction.atomic
def acceptLoad(request, pk_load):
    try:
        load = Load.objects.get(pk=pk_load, status='available')
    except:
        messages.error(request, 'ERROR: This load is not available anymore')
        return redirect('carrier:home')

    carrier = CarrierUser.objects.get(user_id=request.user.id)
    load.accept_load(carrier)
    messages.success(request, 'Load accepted successfully')
    return redirect('carrier:home')


@login_required
@transaction.atomic
def rejectLoad(request, pk_load):
    try:
        load = Load.objects.get(pk=pk_load, status='available')
    except:
        messages.error(request, 'ERROR: This load is not available anymore')
        return redirect('carrier:home')

    carrier = CarrierUser.objects.get(user_id=request.user.id)
    RejectedLoad.objects.create(load=load, carrier=carrier)
    messages.success(request, 'Load rejected successfully')
    return redirect('carrier:home')


@login_required
@transaction.atomic
def dropLoad(request, pk_load):
    try:
        carrier = CarrierUser.objects.get(user_id=request.user.id)
        load = Load.objects.get(pk=pk_load, status='accepted', carrier=carrier)
    except:
        messages.error(request, 'ERROR: This load is not accepted by you')
        return redirect('carrier:home')

    load.drop_load()
    RejectedLoad.objects.create(load=load, carrier=carrier)
    messages.success(request, 'Load dropped successfully')
    return redirect('carrier:home')
