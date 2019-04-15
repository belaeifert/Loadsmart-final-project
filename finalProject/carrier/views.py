from django.shortcuts import render, redirect
from .models import Load, RejectedLoad
from django.contrib.auth.decorators import login_required


@login_required
def list_loads(request):
    pk_carrier = request.user.id

    rej_loads = RejectedLoad.objects.filter(id_carrier=pk_carrier)

    available_loads = Load.objects.filter(status='available').exclude(
        id__in=rej_loads.values('id_load'))
    accepted_loads = Load.objects.filter(
        status='accepted', id_carrier=pk_carrier)
    rejected_loads = Load.objects.filter(id__in=rej_loads.values('id_load'))

    return render(request, 'carrier_abas.html', {
        'available_loads': available_loads,
        'accepted_loads': accepted_loads,
        'rejected_loads': rejected_loads})


def accept_load(request, pk_load):
    load = Load.objects.get(pk=pk_load)
    load.status = 'accepted'
    load.id_carrier = request.user.id
    load.save()
    return redirect('carrier:list_loads')


def reject_load(request, pk_load):
    rej_load = RejectedLoad.objects.create(
        id_load=pk_load, id_carrier=request.user.id)
    return redirect('carrier:list_loads')


def drop_load(request, pk_load):
    load = Load.objects.get(pk=pk_load)
    load.status = 'available'
    load.id_carrier = None
    load.save()

    drop_load = RejectedLoad.objects.create(
        id_load=pk_load, id_carrier=request.user.id)

    return redirect('carrier:list_loads')
