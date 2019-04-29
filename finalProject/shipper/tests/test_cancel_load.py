from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.urls import reverse

from finalProject.shipper.models import Load
from finalProject.shipper.tests.create_user_setUp import create_user

class CancelLoadGet(TestCase):

    def setUp(self):
        user, shipper = create_user()
        self.client.force_login(user)

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

        self.response = self.client.get(r('shipper:cancel_load', self.obj.pk))


    def test_template(self):
        self.assertTemplateUsed(self.response, 'cancel_load_modal.html')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

class CancelLoadDelete(TestCase):
    def setUp(self):
        user, shipper = create_user()
        self.client.force_login(user)

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

        self.response = self.client.post(r('shipper:cancel_load', self.obj.pk))
        self.obj.refresh_from_db()

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    #def test_update(self):
    #    self.assertFalse(Load.objects.exists())
