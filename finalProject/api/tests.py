from django.shortcuts import resolve_url as r
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, APIClient

from finalProject.account.models import User
from finalProject.carrier.models import CarrierUser, RejectedLoad
from finalProject.shipper.models import ShipperUser, Load

factory = APIRequestFactory()

def create_user(is_shipper):
    if is_shipper:
        user = User.objects.create(email='shipper@teste.com', first_name='shipper', last_name='teste', password='123')
        user.save()
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

class ListCarrierAvailableLoads(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper=self.shipper,
        )
        self.obj.save()
        self.response = self.client.get(r('api:list_carrier_available'), format='json')


    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_available_loads(self):
        self.assertEqual(len(self.response.data['results']), Load.objects.filter(status='available').count())

    def test_json(self):
        pass

class ListCarrierAcceptedLoads(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="accepted",
            suggested_price=67.04,
            shipper=self.shipper,
            carrier=self.carrier
        )
        self.obj.save()
        self.response = self.client.get(r('api:list_carrier_accepted'), format='json')


    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_accepted_loads(self):
        self.assertEqual(len(self.response.data['results']), Load.objects.filter(carrier=self.carrier, status='accepted').count())

    def test_json(self):
        pass

class ListCarrierRejectedLoads(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper=self.shipper,
        )
        self.obj.save()
        self.response = self.client.get(r('api:list_carrier_rejected'), format='json')


    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_rejected_loads(self):
        self.assertEqual(len(self.response.data['results']), RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_json(self):
        pass

class AcceptLoadTest(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper=self.shipper,
        )
        self.obj.save()
        self.response = self.client.put(r('api:accept_load', pk_load=self.obj.pk), format='json')


    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        print(self.response)

    def test_accepted_loads(self):
        self.assertTrue(Load.objects.filter(carrier=self.carrier, status='accepted').count())

    def test_json(self):
        pass



class RejectedLoadTest(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper=self.shipper,
        )
        self.obj.save()
        self.response = self.client.put(r('api:reject_load', pk_load=self.obj.pk), format='json')


    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_rejected_load(self):
        self.assertTrue(RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_json(self):
        pass

class DropLoadTest(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="accepted",
            suggested_price=67.04,
            shipper=self.shipper,
            carrier=self.carrier
        )
        self.obj.save()
        self.response = self.client.put(r('api:drop_load', pk_load=self.obj.pk), format='json')


    def test_status_code_drop_load(self):
        self.assertEqual(self.response.status_code, 200)

    def test_reject_load(self):
        self.assertTrue(RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_status_load(self):
        self.assertTrue(Load.objects.filter(pk=self.obj.id, status='available').count())

    def test_json(self):
        pass


class ListShipperAvailableLoads(TestCase):
    def setUp(self):
        self.user, self.shipper = create_user(True)
        self.client = set_auth_client(self.user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper=self.shipper
        )
        self.obj.save()
        self.response = self.client.get(r('api:list_shipper_available'), format='json')

    def test_status_code_available_loads(self):
        self.assertEqual(self.response.status_code, 200)

    def test_available_loads(self):
        self.assertEqual(len(self.response.data['results']), Load.objects.filter(shipper=self.shipper, status='available').count())

    def test_json(self):
        pass

class ListShipperAcceptedLoads(TestCase):
    def setUp(self):
        self.user, self.shipper = create_user(True)
        self.client = set_auth_client(self.user)

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="accepted",
            suggested_price=67.04,
            shipper=self.shipper
        )
        self.obj.save()
        self.response = self.client.get(r('api:list_shipper_accepted'), format='json')

    def test_status_code_available_loads(self):
        self.assertEqual(self.response.status_code, 200)

    def test_available_loads(self):
        self.assertEqual(len(self.response.data['results']), Load.objects.filter(shipper=self.shipper, status='accepted').count())

    def test_json(self):
        pass

class PostLoadTest(APITestCase):
    def setUp(self):
        self.user, self.shipper = create_user(True)
        self.client = set_auth_client(self.user)

        self.response = self.client.post(r("api:post_load"),
                                    {"pickup_date":"2019-03-19", "ref" : 11111, "origin_city":"Miami, FL, USA", "destination_city":"Mesa, AZ, USA", "price":1111},
                                    format='json')
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_load(self):
        self.assertTrue(Load.objects.exists())

    def test_response_json(self):
        self.assertEqual({'success': 'Load posted successfully'}, self.response.json())
