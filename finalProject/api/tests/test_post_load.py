from django.shortcuts import resolve_url as r
from django.test import TestCase
from finalProject.shipper.models import Load
from finalProject.api.tests.auth_setUp import create_user, set_auth_client

class PostLoadSuccessfulTest(TestCase):
    def setUp(self):
        self.user, self.shipper = create_user(True)
        self.client = set_auth_client(self.user)

        self.response = self.client.post(r("api:post_load"),
                                    {
                                        "pickup_date":"2019-03-19",
                                        "ref" : 11111,
                                        "origin_city":"Miami, FL, USA",
                                        "destination_city":"Mesa, AZ, USA",
                                        "price":1111,
                                    },
                                    format='json')
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_load(self):
        self.assertTrue(Load.objects.exists())

    def test_response_json(self):
        self.assertEqual(self.response.json(), {'success': 'Load posted successfully'})
