from django.test import TestCase
from finalProject.account.models import User
import unittest



class UserModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='carrier@teste.com', first_name='carrier', last_name='doe', password='teste1234')

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))

    def test_carrier_atribute(self):
        self.assertEqual(self.user.email, 'carrier@teste.com')

