from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from finalProject.account.models import User
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser


def create_user(is_shipper):
    if is_shipper:
        user = User.objects.create(email='shipper@teste.com', first_name='shipper', last_name='teste', password='123')
        shipper = ShipperUser.objects.create(user=user)
        shipper.save()
        return user, shipper
    else:
        user = User.objects.create(email='carrier@teste.com', first_name='carrier', last_name='teste', password='123')
        carrier = CarrierUser.objects.create(user=user, MC_number=123)
        carrier.save()
        return user, carrier


def set_auth_client(user):
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client
