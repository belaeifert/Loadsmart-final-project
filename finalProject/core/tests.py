from django.shortcuts import resolve_url as r
from django.test import TestCase


class GetIndexTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('index'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed('index.html')
