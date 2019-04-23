from django.test import TestCase

# Create your tests here.
from finalProject.shipper.forms import LoadForm
from finalProject.shipper.models import Load


class DashboardGetTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/shipper/dashboard/')

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

class PostLoadTest(TestCase):

    def setUp(self):
        self.obj = Load(
            pickup_date = '2019-04-17',
            ref = 123
            origin_city = 'Miami Gardens, FL, USA',
            destination_city = 'Florida City, FL, USA',
            price = 50.0,

        )


    def test_post_load (self):
        ''' Valid post should return to shipper dashboard'''
        self.assertEqual(200, self.response.status_code)