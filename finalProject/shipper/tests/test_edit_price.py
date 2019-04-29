from django.test import TestCase
from django.shortcuts import resolve_url as r

from finalProject.shipper.models import Load
from finalProject.shipper.tests.create_user_setUp import create_user


class EditPriceGet(TestCase):

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

        self.response = self.client.get(r('shipper:edit_price', self.obj.pk))


    def test_template(self):
        self.assertTemplateUsed(self.response, 'edit_price_modal.html')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

class EditPricePut(TestCase):
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

        self.response = self.client.post(r('shipper:edit_price', self.obj.pk), {'price':67.04})
        self.obj.refresh_from_db()

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_update(self):
        self.assertEqual(self.obj.price, 67.04)

