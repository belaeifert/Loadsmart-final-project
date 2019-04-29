from django.test import TestCase
from django.shortcuts import resolve_url as r
from finalProject.account.models import User
from finalProject.carrier.models import CarrierUser


class GetCarrierRegistrationTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('account:carrier_signup'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed('signup_form.html')


class PostCarrierRegistration(TestCase):
    def setUp(self):
        data = {
            'email':'carrier@teste.com',
            'first_name': 'carrier',
            'last_name': 'teste',
            'mc_numb':123,
            'password1':'testando',
            'password2':'testando'
        }
        self.response = self.client.post(r('account:carrier_signup'), data=data)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_created_user(self):
        print(User.objects.all())
        self.assertTrue(CarrierUser.objects.get(pk=1))





