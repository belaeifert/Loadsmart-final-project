from datetime import date

from django.test import TestCase

# Create your tests here.
from finalProject.account.models import User
from finalProject.shipper.forms import LoadForm
from finalProject.shipper.models import Load, ShipperUser

'''
class HomeGetTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/shipper/home/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'dashboard.html')

    def test_html(self):
        self.assertContains(self.response, '<form')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, LoadForm)
'''


class PostLoadTest(TestCase):

    def setUp(self):
        user = User(
            first_name='Mary',
            last_name='Smith',
            email='mary@smith.com'
        )
        user.save()

        self.shipper = ShipperUser(
            user=user
        )
        self.shipper.save()

        self.obj = Load(
            pickup_date='2019-04-17',
            ref=123,
            origin_city='Miami Gardens, FL, USA',
            destination_city='Florida City, FL, USA',
            price=50.0,
            status="available",
            suggested_price=67.04,
            shipper= self.shipper
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Load.objects.exists())

    def test_str(self):
        test_str = "Pickup date: {}, REF: {}, Origin City: {}, Destination city: {}, Price: {}, Carrier: {}, Shipper: {}".format(
            self.obj.pickup_date, self.obj.ref, self.obj.origin_city, self.obj.destination_city,
            self.obj.price, self.obj.carrier, self.obj.shipper)
        self.assertEqual(test_str, str(self.obj))
'''
    def test_post_load(self):
         Valid post should return to shipper home
        self.assertEqual(200, self.response.status_code)
        '''

class CreateShipperUserTest(TestCase):

    def setUp(self):
        user = User(
            first_name='Mary',
            last_name='Smith',
            email='mary@smith.com'
        )
        user.save()

        self.obj = ShipperUser(
            user=user
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(ShipperUser.objects.exists())

    def test_str(self):
        test_str = "shipper id: {}, user id: {}, Name: {}".format(self.obj.pk, self.obj.user.pk, self.obj.user.first_name)
        self.assertEqual(test_str, str(self.obj))
