from django.shortcuts import resolve_url as r
from django.test import TestCase

from finalProject.account.models import User
from finalProject.carrier.models import CarrierUser, RejectedLoad
from finalProject.shipper.models import Load, ShipperUser


def createCarrierUser():
    user = User.objects.create(
        email='carrier@teste.com',
        first_name='carrier',
        last_name='teste')
    user.save()

    carrier = CarrierUser.objects.create(
        user=user,
        MC_number='12345')
    carrier.save()

    return user


def createLoad():
    user = User.objects.create(
        email='shipper@teste.com',
        first_name='shipper',
        last_name='teste')
    user.save()
    shipper = ShipperUser.objects.create(user=user)
    shipper.save()

    load = Load(
        pickup_date='2019-06-10',
        ref=123,
        origin_city='Miami Gardens, FL, USA',
        destination_city='Florida City, FL, USA',
        price=50.0,
        status="available",
        suggested_price=67.04,
        shipper=shipper,
    )
    load.save()

    return load


class CarrierHomeGet(TestCase):

    def setUp(self):
        user = createCarrierUser()
        self.client.force_login(user)
        self.response = self.client.get(r('carrier:home'))

    def test_template(self):
        self.assertTemplateUsed(self.response, 'carrier_home.html')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)


class CarrierAcceptLoadTest(TestCase):

    def setUp(self):
        user = createCarrierUser()
        self.client.force_login(user)

        self.load = createLoad()

        self.response = self.client.get(
            r('carrier:accept_load', pk_load=self.load.pk), follow=True)

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'carrier_home.html')

    def test_status_load(self):
        self.load.refresh_from_db()
        self.assertEqual(self.load.status, 'accepted')

    def test_accepted_loads_is_one(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['accepted_loads']), 1)

    def test_available_loads_is_zero(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['available_loads']), 0)


class CarrierRejectLoadTest(TestCase):

    def setUp(self):
        user = createCarrierUser()
        self.client.force_login(user)

        self.load = createLoad()

        self.response = self.client.get(
            r('carrier:reject_load', pk_load=self.load.pk), follow=True)

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'carrier_home.html')

    def test_status_load(self):
        self.load.refresh_from_db()
        self.assertEqual(self.load.status, 'available')

    def test_rejected_loads_is_one(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['rejected_loads']), 1)

    def test_available_loads_is_zero(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['available_loads']), 0)


class CarrierDropLoadTest(TestCase):

    def setUp(self):
        user = createCarrierUser()
        self.client.force_login(user)

        self.load = createLoad()
        self.load.status = 'accepted'
        self.load.carrier = CarrierUser.objects.get(user_id=user.pk)
        self.load.save()

        self.response = self.client.get(
            r('carrier:drop_load', pk_load=self.load.pk), follow=True)

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'carrier_home.html')

    def test_status_load(self):
        self.load.refresh_from_db()
        self.assertEqual(self.load.status, 'available')

    def test_rejected_loads_is_one(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['rejected_loads']), 1)

    def test_accepted_loads_is_zero(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['accepted_loads']), 0)

    def test_available_loads_is_zero(self):
        self.response = self.client.get(r('carrier:home'))
        self.assertEqual(len(self.response.context['available_loads']), 0)


class CarrierUserModelTests(TestCase):

    def setUp(self):
        user = createCarrierUser()
        self.carrier = CarrierUser.objects.get(user_id=user.pk)

    def test_carrier_creation(self):
        self.assertTrue(isinstance(self.carrier, CarrierUser))

    def test_carrier_email(self):
        self.assertEqual(self.carrier.user.email, 'carrier@teste.com')

    def test_carrier_MC_number(self):
        self.assertEqual(self.carrier.MC_number, 12345)


class RejectedLoadModelTests(TestCase):

    def setUp(self):
        user = createCarrierUser()
        self.carrier = CarrierUser.objects.get(user_id=user.pk)

        self.load = createLoad()

        self.rej_load = RejectedLoad.objects.create(
            load=self.load, carrier=self.carrier)

    def test_rejected_load_creation(self):
        self.assertTrue(isinstance(self.rej_load, RejectedLoad))

    def test_rejected_load_origin_city(self):
        self.assertEqual(self.rej_load.load.origin_city,
                         'Miami Gardens, FL, USA')
