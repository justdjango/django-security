from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.shortcuts import reverse
from accounts.models import Column, Subscription
from accounts.tests.common.mixins import ColumnTestDataMixin
from accounts import views

User = get_user_model()


class ColumnListViewTest(TestCase):
    fixtures = [
        'users.json',
        'columns.json'
    ]

    def test_get_column_list(self):
        response = self.client.get(reverse("columns:column-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "a test column")
        self.assertContains(response, "Column list")


class ColumnFeedViewTest(TestCase):
    fixtures = [
        'users.json',
        'columns.json',
        'subscriptions.json'
    ]

    def setUp(self):
        self.factory = RequestFactory()
        self.reader = User.objects.get(email="reader@jd.com")

    def test_get_column_feed(self):
        request = self.factory.get(reverse("columns:feed"))
        request.user = self.reader

        # request.user = AnonymousUser()
        response = views.ColumnFeedView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        column_names = list(request.user.user_subscriptions.all().values_list(
            'column__name', flat=True
        ))

        for name in column_names:
            self.assertContains(response, name)


# class DemoTest(TestCase):
#     """
#     setUp
#     setUpClass
#     setUpTestData

#     """

#     def setUp(self):
#         """Once per test"""
#         pass

#     def setUpClass(cls):
#         """Once per TestCase class"""
#         pass

#     def setUpTestData(cls):
#         """Once per TestCase class"""
#         pass

#     def test_some_func(self):
#         pass

#     def tearDown(self):
#         """Once per test"""
#         pass

#     def tearDownClass(cls):
#         """Once per TestCase class"""
#         pass
