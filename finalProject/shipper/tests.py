from datetime import date
from django.test import TestCase, Client
from django.urls import reverse

from finalProject import settings
from finalProject.account.models import User
from finalProject.shipper.forms import LoadForm
from finalProject.shipper.models import Load, ShipperUser
from django.shortcuts import resolve_url as r

def create_user():
    user = User.objects.create(email='shipper@teste.com', first_name='shipper', last_name='teste')
    user.save()

    shipper = ShipperUser.objects.create(user=user)
    shipper.save()

    return user


class ShipperHomeGet(TestCase):

    def setUp(self):
        user = create_user()
        self.client.force_login(user)
        self.response = self.client.get(r('shipper:home'))


    def test_template(self):
        self.assertTemplateUsed(self.response, 'shipper_home.html')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_google_api_key(self):
        self.assertEqual(self.response.context['api_key'], settings.GOOGLE_API_KEY)


class PostLoadGet(TestCase):

    def setUp(self):
        user = create_user()
        self.client.force_login(user)
        self.response = self.client.get(r('shipper:post_load'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)


    def test_template(self):
        self.assertTemplateUsed(self.response, 'post-load.html')


    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


    def test_post_load_html(self):
        tags = (
            ('<form', 1),
            ('input', 7),
            ('type="date"', 1),
            ('type="text"', 4),
            ('type="number"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, LoadForm)



class PostLoadTest(TestCase):

    def setUp(self):
        user = create_user()
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

    def test_create(self):
        ''' Data from valid Post must exist in database'''
        self.assertTrue(Load.objects.exists())

    def test_str(self):
        test_str = "Pickup date: {}, REF: {}, Origin City: {}, Destination city: {}, Price: {}, Carrier: {}, Shipper: {}".format(
            self.obj.pickup_date, self.obj.ref, self.obj.origin_city, self.obj.destination_city,
            self.obj.price, self.obj.carrier, self.obj.shipper)
        self.assertEqual(str(self.obj), test_str)



