from django.shortcuts import resolve_url as r
from django.test import TestCase

from finalProject.account.models import User
from finalProject.api.tests.auth_setUp import create_user, set_auth_client
from finalProject.carrier.models import CarrierUser, RejectedLoad
from finalProject.shipper.models import Load


class AcceptLoadSuccessfulTest(TestCase):
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

    def test_accepted_load(self):
        self.assertTrue(Load.objects.filter(carrier=self.carrier, status='accepted').count())

    def test_json_successful(self):
        self.assertEqual(self.response.data, {'success': 'Load accepted successfully'})


class AcceptLoadUnsuccessfulTest(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        another_user = User.objects.create(email='carrier2@teste.com', first_name='carrier 2', last_name='teste',
                                           password='123')
        another_carrier = CarrierUser.objects.create(user=another_user, MC_number=456)
        another_carrier.save()

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="accepted",
            suggested_price=67.04,
            shipper=self.shipper,
            carrier=another_carrier
        )
        self.obj.save()
        self.response = self.client.put(r('api:accept_load', pk_load=self.obj.pk), format='json')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 404)

    def test_accepted_loads(self):
        self.assertFalse(Load.objects.filter(carrier=self.carrier, status='accepted').count())

    def test_json_unsuccessful(self):
        self.assertEqual(self.response.data, {'error': 'Load not found or Load not available'})


class RejectLoadSuccessfulTest(TestCase):
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

    def test_reject_load(self):
        self.assertTrue(RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_json_successful(self):
        self.assertEqual(self.response.data, {'success': 'Load rejected successfully'})


class RejectLoadUnsuccessfulTest(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        another_user = User.objects.create(email='carrier2@teste.com', first_name='carrier 2', last_name='teste',
                                           password='123')
        another_carrier = CarrierUser.objects.create(user=another_user, MC_number=456)
        another_carrier.save()

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="accepted",
            suggested_price=67.04,
            shipper=self.shipper,
            carrier=another_carrier
        )
        self.obj.save()
        self.response = self.client.put(r('api:reject_load', pk_load=self.obj.pk), format='json')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 404)

    def test_rejected_load(self):
        self.assertFalse(RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_json_unsuccessful(self):
        self.assertEqual(self.response.data, {'error': 'Load not found or Load not available'})


class DropLoadSuccessfulTest(TestCase):
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

    def test_json_successful(self):
        self.assertEqual(self.response.data, {'success': 'Load dropped successfully'})


class DropLoadUnsuccessfulTest(TestCase):
    def setUp(self):
        self.shipper_user, self.shipper = create_user(True)
        self.carrier_user, self.carrier = create_user(False)

        self.client = set_auth_client(self.carrier_user)

        another_user = User.objects.create(email='carrier2@teste.com', first_name='carrier 2', last_name='teste',
                                           password='123')
        another_carrier = CarrierUser.objects.create(user=another_user, MC_number=456)
        another_carrier.save()

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="accepted",
            suggested_price=67.04,
            shipper=self.shipper,
            carrier=another_carrier
        )
        self.obj.save()
        self.response = self.client.put(r('api:drop_load', pk_load=self.obj.pk), format='json')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 404)

    def test_rejected_load(self):
        self.assertFalse(RejectedLoad.objects.filter(carrier=self.carrier, load=self.obj).count())

    def test_json_unsuccessful(self):
        self.assertEqual(self.response.data, {'error': 'Load not found or Load is not accepted by you'})
