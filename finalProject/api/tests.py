from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from requests.auth import HTTPBasicAuth
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase, APIClient


from finalProject.account.models import User
from finalProject.api.views import ShipperPostLoad
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser, Load

factory = APIRequestFactory()

def create_user(is_shipper):
    user = User.objects.create(email='shipper@teste.com', first_name='shipper', last_name='teste', password='123')
    user.save()

    if is_shipper:
        shipper = ShipperUser.objects.create(user=user)
    else:
        shipper = CarrierUser.objects.create(user=user)

    shipper.save()

    return user

def set_auth_client(user):
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client

class ShipperTest(APITestCase):
    def setUp(self):
        self.client = set_auth_client(create_user(True))

        self.response = self.client.post(r("api:post_load"),
                                    {"pickup_date":"2019-03-19", "ref" : 11111, "origin_city":"Miami, FL, USA", "destination_city":"Mesa, AZ, USA", "price":1111},
                                    format='json')
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_load(self):
        self.assertTrue(Load.objects.exists())

    def test_response_json(self):
        self.assertEqual({'success': 'Load posted successfully'}, self.response.json())

class ListShipperLoads(TestCase):
    def setUp(self):
        user = create_user(True)
        self.client = set_auth_client(user)
        shipper = ShipperUser.objects.get(user=user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper=shipper
        )
        self.obj.save()
        self.response = self.client.get(r('api:list_accepted'))

    def test_status_code_available_loads(self):
        self.assertEqual(self.response.status_code, 200)

    def test_available_loads(self):
        print(self.response.co)


