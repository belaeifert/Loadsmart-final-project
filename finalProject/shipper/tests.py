from datetime import date
from django.test import TestCase, Client
from django.urls import reverse

from finalProject.account.models import User
from finalProject.shipper.forms import LoadForm
from finalProject.shipper.models import Load, ShipperUser


class ShipperHomeGet(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(email='shipper@teste.com', first_name='shipper', last_name='doe')
        self.user.save()
        self.user.set_password('teste1234')

        self.shipper = ShipperUser.objects.create(user=self.user)
        self.shipper.save()

        #self.client.force_login(self.user)

        self.login = self.client.login(email=self.user.email, password=self.user.password)
        self.response = self.client.get(r'shipper:home')


    def test_template(self):
        print(self.response)
        self.assertTemplateUsed(self.response, 'shipper_home.html')
    '''
    def test_get(self):
        self.assertEqual(302, self.response.status_code)

    
    def test_template(self):
        print(self.response)
        self.assertTemplateUsed(self.response, 'shipper_home.html')

    def test_post_load_html(self):
        tags = (
            ('<form', 1),
            ('input', 7),
            ('type="date"', 1),
            ('type=text', 4),
            ('type=decimal', 1),
            ('type=submit', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, LoadForm)

    def test_post_load_html(self):
        self.assertContains(self.response, '<form')
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
        ''' Data from valid Post must exist in database'''
        self.assertTrue(Load.objects.exists())

    def test_str(self):
        test_str = "Pickup date: {}, REF: {}, Origin City: {}, Destination city: {}, Price: {}, Carrier: {}, Shipper: {}".format(
            self.obj.pickup_date, self.obj.ref, self.obj.origin_city, self.obj.destination_city,
            self.obj.price, self.obj.carrier, self.obj.shipper)
        self.assertEqual(test_str, str(self.obj))

    #def test_post_load(self):
    #    ''' Valid Post must return status code 200 '''
    #    self.assertEqual(200, self.response.status_code)


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
