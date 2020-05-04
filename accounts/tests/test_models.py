from django.contrib.auth import get_user_model
from django.test import TestCase
from accounts.models import UserProfile


User = get_user_model()


class UserProfileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(email="test@test.com", password="test1234")

    def setUp(self):
        self.user = User.objects.get(email="test@test.com")

    def test_create_userprofile(self):
        userprofile = UserProfile.objects.get(user=self.user)
        self.assertTrue(isinstance(userprofile, UserProfile))
        self.assertEqual(userprofile.__str__(), self.user.email)
        self.assertEqual(userprofile.user_type, "Reader")
