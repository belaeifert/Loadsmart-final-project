from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from finalProject.api.serializers import LoadSerializer
from finalProject.api.permissions import IsCarrier, IsShipper
from finalProject.shipper.models import Load, ShipperUser
from finalProject.carrier.models import CarrierUser, RejectedLoad


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_token(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class CarrierAvailableLoads(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCarrier,)
    serializer_class = LoadSerializer

    def get_queryset(self):
        carrier = CarrierUser.objects.get(user_id=self.request.user.id)
        rej_loads = RejectedLoad.objects.filter(carrier=carrier)
        available_loads = Load.objects.filter(status='available').exclude(
            id__in=rej_loads.values('load_id'))
        return available_loads

class CarrierAcceptedLoads(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCarrier,)
    serializer_class = LoadSerializer

    def get_queryset(self):
        carrier = CarrierUser.objects.get(user_id=self.request.user.id)
        accepted_loads = Load.objects.filter(
            status='accepted', carrier=carrier)
        return accepted_loads


class CarrierRejectedLoads(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCarrier,)
    serializer_class = LoadSerializer

    def get_queryset(self):
        carrier = CarrierUser.objects.get(user_id=self.request.user.id)
        rej_loads = RejectedLoad.objects.filter(carrier=carrier)
        rejected_loads = Load.objects.filter(id__in=rej_loads.values('load_id'))
        return rejected_loads


@api_view(["POST"])
@permission_classes((IsAuthenticated, IsCarrier,))
def CarrierAccept(request, pk_load):
    try:
        load = Load.objects.get(pk=pk_load, status='available')
    except:
        return Response({'error': 'Load not found or Load not available'},
                        status=HTTP_404_NOT_FOUND)

    carrier = CarrierUser.objects.get(user_id=request.user.id)
    load.accept_load(carrier)
    return Response({'success': 'Load accepted successfully'},
                    status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((IsAuthenticated, IsCarrier,))
def CarrierReject(request, pk_load):
    try:
        load = Load.objects.get(pk=pk_load, status='available')
    except:
        return Response({'error': 'Load not found or Load not available'},
                        status=HTTP_404_NOT_FOUND)

    carrier = CarrierUser.objects.get(user_id=request.user.id)
    rej_load = RejectedLoad.objects.create(load=load, carrier=carrier)
    return Response({'success': 'Load rejected successfully'},
                    status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((IsAuthenticated, IsCarrier,))
def CarrierDrop(request, pk_load):
    try:
        carrier = CarrierUser.objects.get(user_id=request.user.id)
        load = Load.objects.get(pk=pk_load, status='accepted', carrier=carrier)
    except:
        return Response({'error': 'Load not found or Load is not accepted by you'},
                        status=HTTP_404_NOT_FOUND)
    
    load.drop_load()
    drop_load = RejectedLoad.objects.create(load=load, carrier=carrier)
    return Response({'success': 'Load dropped successfully'},
                    status=HTTP_200_OK)


class ShipperAvailableLoads(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsShipper,)
    serializer_class = LoadSerializer

    def get_queryset(self):
        shipper = ShipperUser.objects.get(user_id=self.request.user.id)
        available_loads = Load.objects.filter(status='available', shipper=shipper)
        return available_loads


class ShipperAcceptedLoads(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsShipper,)
    serializer_class = LoadSerializer

    def get_queryset(self):
        shipper = ShipperUser.objects.get(user_id=self.request.user.id)
        accepted_loads = Load.objects.filter(status='accepted', shipper=shipper)
        return accepted_loads


@api_view(["POST"])
@permission_classes((IsAuthenticated, IsShipper,))
def ShipperPostLoad(request):
    serializer = LoadSerializer(data=request.data)

    if serializer.is_valid():
        shipper = ShipperUser.objects.get(user_id=request.user.id)
        serializer.save(shipper=shipper)
        return Response({'success': 'Load posted successfully'},
                        status=HTTP_200_OK)
    return Response(serializer.errors,
                    status=HTTP_400_BAD_REQUEST)
