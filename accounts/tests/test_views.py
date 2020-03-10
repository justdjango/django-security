from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):

    def test_get(self):
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        url = reverse('home')
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 200)


class TestSessionRequiringView(TestCase):

    def test_valid_param(self):
        url = reverse('session-view', kwargs={'payment_id': 348329482})
        resp = self.client.get(url)
        self.assertContains(resp, "Your payment id is here")

    def test_invalid_param(self):
        url = reverse('session-view', kwargs={'payment_id': 123321})
        resp = self.client.get(url)
        self.assertContains(resp, "Your payment id is not here")
