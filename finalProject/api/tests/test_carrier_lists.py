from django.test import TestCase
from django.shortcuts import resolve_url as r
from finalProject.api.tests.auth_setUp import create_user, set_auth_client
from finalProject.carrier.models import RejectedLoad
from finalProject.shipper.models import Load



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
        self.assertEqual(self.response.json()['results'][0],
                         {
                             'id': 1,
                             'pickup_date': '2019-04-17',
                             'ref': '123',
                             'origin_city': 'Miami Gardens, FL, USA',
                             'destination_city': 'Florida City, FL, USA',
                             'price': 47.5, 'status': 'available',
                             'shipper': 'shipper teste',
                             'carrier': None}
                         )



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
        self.assertEqual(self.response.json()['results'][0],
                         {
                             'id': 1,
                             'pickup_date': '2019-04-17',
                             'ref': '123',
                             'origin_city': 'Miami Gardens, FL, USA',
                             'destination_city': 'Florida City, FL, USA',
                             'price': 47.5,
                             'status': 'accepted',
                             'shipper': 'shipper teste',
                             'carrier': 'carrier teste'
                         })

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

        self.obj_rejected = RejectedLoad(load=self.obj, carrier=self.carrier)
        self.obj_rejected.save()

        self.response = self.client.get(r('api:list_carrier_rejected'), format='json')


    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_rejected_loads(self):
        self.assertEqual(len(self.response.data['results']), RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_json(self):
        self.assertEqual(self.response.json()['results'][0],
            {
                'id': 1,
                'pickup_date': '2019-04-17',
                'ref': '123',
                'origin_city': 'Miami Gardens, FL, USA',
                'destination_city': 'Florida City, FL, USA',
                'price': 47.5,
                'status': 'available',
                'shipper': 'shipper teste',
                'carrier': None
            })