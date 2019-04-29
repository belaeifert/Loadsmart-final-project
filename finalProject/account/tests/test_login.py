from django.test import TestCase

from finalProject.account.models import User
from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser
from django.shortcuts import resolve_url as r



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

class GetLoginTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('account:login'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed('login.html')

class PostShipperLoginTest(TestCase):
    def setUp(self):
        user, shipper = create_user(True)
        data = {
            'email': 'shipper@teste.com',
            'password': 123,
        }
        self.response = self.client.post(r('account:login'), data)

    #def test_status_code(self):
    #    self.assertEqual(self.response.status_code, 302)

