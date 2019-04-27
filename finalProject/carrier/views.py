from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from finalProject.shipper.models import Load
from finalProject.carrier.models import RejectedLoad, CarrierUser


@login_required
def list_loads(request):
    carrier = CarrierUser.objects.get(user_id=request.user.id)

    rej_loads = RejectedLoad.objects.filter(carrier=carrier)
    available_loads = Load.objects.filter(status='available').exclude(
        id__in=rej_loads.values('load_id'))
    accepted_loads = Load.objects.filter(
        status='accepted', carrier=carrier)
    rejected_loads = Load.objects.filter(id__in=rej_loads.values('load_id'))

    return render(request, 'carrier_abas.html', {
        'available_loads': available_loads,
        'accepted_loads': accepted_loads,
        'rejected_loads': rejected_loads})


@login_required
@transaction.atomic
def accept_load(request, pk_load):
    try:
        load = Load.objects.get(pk=pk_load, status='available')
    except:
        messages.error(request, 'ERROR: This load is not available anymore')
        return redirect('carrier:list_loads')

    carrier = CarrierUser.objects.get(user_id=request.user.id)
    load.accept_load(carrier)
    messages.success(request, 'Load accepted successfully')
    return redirect('carrier:list_loads')


@login_required
@transaction.atomic
def reject_load(request, pk_load):
    try:
        load = Load.objects.get(pk=pk_load, status='available')
    except:
        messages.error(request, 'ERROR: This load is not available anymore')
        return redirect('carrier:list_loads')

    carrier = CarrierUser.objects.get(user_id=request.user.id)
    rej_load = RejectedLoad.objects.create(load=load, carrier=carrier)
    messages.success(request, 'Load rejected successfully')
    return redirect('carrier:list_loads')


@login_required
@transaction.atomic
def drop_load(request, pk_load):
    try:
        carrier = CarrierUser.objects.get(user_id=request.user.id)
        load = Load.objects.get(pk=pk_load, status='accepted', carrier=carrier)
    except:
        messages.error(request, 'ERROR: This load is not accepted by you')
        return redirect('carrier:list_loads')

    load.drop_load()
    drop_load = RejectedLoad.objects.create(load=load, carrier=carrier)
    messages.success(request, 'Load dropped successfully')
    return redirect('carrier:list_loads')
