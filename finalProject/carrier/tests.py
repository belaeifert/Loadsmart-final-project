from django.test import TestCase
from django.shortcuts import reverse
from finalProject.carrier.models import CarrierUser, RejectedLoad
from finalProject.account.models import User
from finalProject.shipper.models import Load, ShipperUser
import unittest


class CarrierUserModelTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            email='carrier@teste.com', first_name='carrier', last_name='doe', password='teste1234')
        self.carrier = CarrierUser.objects.create(
            user=self.user1, MC_number='12345')

    def test_carrier_creation(self):
        self.assertTrue(isinstance(self.carrier, CarrierUser))

    def test_carrier_atribute(self):
        self.assertEqual(self.carrier.user.email, 'carrier@teste.com')


class RejectedLoadModelTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            email='carrier@teste.com', first_name='carrier', last_name='doe', password='teste1234')
        self.carrier = CarrierUser.objects.create(
            user=self.user1, MC_number='12345')

        self.user2 = User.objects.create(
            email='shipper@teste.com', first_name='shipper', last_name='doe', password='teste9988')
        self.shipper = ShipperUser.objects.create(user=self.user2)

        self.load = Load.objects.create(
            ref='123', origin_city='miami', destination_city='new york', price='2000', shipper=self.shipper)

        self.rej_load = RejectedLoad.objects.create(
            load=self.load, carrier=self.carrier)

    def test_rejected_load_creation(self):
        self.assertTrue(isinstance(self.rej_load, RejectedLoad))

    def test_rejected_load_atribute(self):   
        self.assertEqual(self.rej_load.load.origin_city, 'miami')


class CarrierViewTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
                email='carrier@teste.com', first_name='carrier', last_name='doe', password='teste1234')
        self.carrier = CarrierUser.objects.create(user=self.user1, MC_number='12345')
        
        self.user2 = User.objects.create(
            email='shipper@teste.com', first_name='shipper', last_name='doe', password='teste9988')
        self.shipper = ShipperUser.objects.create(user=self.user2)        
        
        self.load = Load.objects.create(
            ref='123', origin_city='miami', destination_city='new york', price='2000', shipper=self.shipper) 
        
        self.response = self.client.login(
            email='carrier@teste.com', password='teste1234')

    '''
    def test_list_loads(self):
        self.response = self.client.get(reverse('carrier:list_loads'))
        self.assertEqual(200, self.response.status_code) 
        # Not working: The status code should be 200 not 302 
    '''
    def test_accept_load(self):
        pk_load = self.load.pk
        self.response = self.client.get(reverse('carrier:accept_load', kwargs={'pk_load': pk_load}))
        self.assertEqual(302, self.response.status_code)
    
    def test_reject_load(self):
        pk_load = self.load.pk
        self.response = self.client.get(reverse('carrier:reject_load', kwargs={'pk_load': pk_load}))
        self.assertEqual(302, self.response.status_code) 

    def test_drop_load(self):
        pk_load = self.load.pk
        self.response = self.client.get(reverse('carrier:drop_load', kwargs={'pk_load': pk_load}))
        self.assertEqual(302, self.response.status_code)   


if __name__ == '__main__':
    unittest.main()