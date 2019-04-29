from django.test import TestCase
from django.shortcuts import resolve_url as r
from finalProject.account.models import User
from finalProject.shipper.models import ShipperUser


class GetShipperRegistrationTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('account:shipper_signup'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed('signup_form.html')


class PostShipperRegistration(TestCase):
    def setUp(self):
        data = {
            'email':'shipper@teste.com',
            'first_name': 'shipper',
            'last_name': 'teste',
            'password1':'testando',
            'password2':'testando'
        }
        self.response = self.client.post(r('account:shipper_signup'), data=data)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_created_user(self):
        print(User.objects.all())
        self.assertTrue(ShipperUser.objects.get(pk=1))





