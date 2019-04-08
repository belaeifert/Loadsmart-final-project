from django.test import TestCase

# Create your tests here.
from finalProject.shipper.forms import LoadForm


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
        data = dict(
            ref='#0123456789',
            origin_city='Miami',
            destination_city='New York',
            price=1000,
        )
        self.response = self.client.post('/shipper/dashboard/', data)


    def test_post_load (self):
        ''' Valid post should return to shipper dashboard'''
        self.assertEqual(200, self.response.status_code)