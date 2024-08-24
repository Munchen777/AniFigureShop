from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


from api.models import User


class TestAuthUser(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("users:login")
        credentials = {
            "email": "admin@gmail.com",
            "username": "admin",
            "password": "MyMacM2",
        }
        self.user = User.objects.create_user(**credentials)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_login_with_email_success(self):
        credentials = {
            "email": "admin@gmail.com",
            "password": "MyMacM2",
        }
        response = self.client.post(
            path=self.url,
            data=credentials,
            format="json"
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)

    def test_login_with_username_success(self):
        credentials = {
            "username": "admin",
            "password": "MyMacM2",
        }
        response = self.client.post(
            path=self.url,
            data=credentials,
            format="json"
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)

    def test_login_with_email_error(self):
        credentials = {
            "email": "user@gmail.com",
            "password": "MyMacM2",
        }
        response = self.client.post(
            path=self.url,
            data=credentials,
            format="json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertNotIn("token", response.data)

    def test_login_with_username_error(self):
        credentials = {
            "username": "adm",
            "password": "MyMacM2",
        }
        response = self.client.post(
            path=self.url,
            data=credentials,
            format="json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertNotIn("token", response.data)
        
        