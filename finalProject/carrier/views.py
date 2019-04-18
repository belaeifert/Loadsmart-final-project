from django.shortcuts import render, redirect
from finalProject.shipper.models import Load
from finalProject.carrier.models import RejectedLoad, CarrierUser
from django.contrib.auth.decorators import login_required


@login_required
def list_loads(request):
    pk_carrier = request.user.id
    print("**********************************************")
    print(pk_carrier)

    rej_loads = RejectedLoad.objects.filter(carrier_id=pk_carrier)
    available_loads = Load.objects.filter(status='available').exclude(
        id__in=rej_loads.values('load_id'))
    accepted_loads = Load.objects.filter(
        status='accepted', carrier_id=pk_carrier)
    rejected_loads = Load.objects.filter(id__in=rej_loads.values('load_id'))

    return render(request, 'carrier_abas.html', {
        'available_loads': available_loads,
        'accepted_loads': accepted_loads,
        'rejected_loads': rejected_loads})


def accept_load(request, pk_load):
    print("****************************************8*******")
    print(CarrierUser.objects.get(user_id=request.user.id))
    carrier = CarrierUser.objects.get(user_id=request.user.id)
    load = Load.objects.get(pk=pk_load)
    load.status = 'accepted'
    load.carrier = carrier
    load.save()
    return redirect('carrier:list_loads')


def reject_load(request, pk_load):
    load = Load.objects.get(pk=pk_load)
    carrier = CarrierUser.objects.get(user_id=request.user.id)
    rej_load = RejectedLoad.objects.create(
        load=load, carrier=carrier)
    return redirect('carrier:list_loads')


def drop_load(request, pk_load):
    load = Load.objects.get(pk=pk_load)
    load.status = 'available'
    load.carrier = None
    load.save()

    carrier = CarrierUser.objects.get(pk=request.user.id)

    drop_load = RejectedLoad.objects.create(
        load=load, carrier=carrier)

    return redirect('carrier:list_loads')
