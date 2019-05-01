from django.shortcuts import resolve_url as r
from django.test import TestCase

from finalProject.api.tests.auth_setUp import createUser, setAuthClient
from finalProject.shipper.models import Load


class ListShipperAvailableLoads(TestCase):
    def setUp(self):
        self.user, self.shipper = createUser(True)
        self.client = setAuthClient(self.user)

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
        self.assertEqual(len(self.response.data['results']),
                         Load.objects.filter(shipper=self.shipper, status='available').count())

    def test_json(self):
        self.assertEqual(self.response.json()['results'][0],
                         {
                             'id': 1,
                             'pickup_date': '2019-04-17',
                             'ref': '123',
                             'origin_city': 'Miami Gardens, FL, USA',
                             'destination_city': 'Florida City, FL, USA',
                             'price': 50.0,
                             'status': 'available',
                             'shipper': 'shipper teste',
                             'carrier': None
                         })


class ListShipperAcceptedLoads(TestCase):
    def setUp(self):
        self.user, self.shipper = createUser(True)
        self.client = setAuthClient(self.user)

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

    def test_status_code_accepted_loads(self):
        self.assertEqual(self.response.status_code, 200)

    def test_accepted_loads(self):
        self.assertEqual(len(self.response.data['results']),
                         Load.objects.filter(shipper=self.shipper, status='accepted').count())

    def test_json(self):
        self.assertEqual(self.response.json()['results'][0],
                         {
                             'id': 1,
                             'pickup_date': '2019-04-17',
                             'ref': '123',
                             'origin_city': 'Miami Gardens, FL, USA',
                             'destination_city': 'Florida City, FL, USA',
                             'price': 50.0,
                             'status': 'accepted',
                             'shipper': 'shipper teste',
                             'carrier': None
                         })
