from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import AccountsModel
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class Test_add_user(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_servername = "test_servername"
        cls.test_user_login_id = "11111111"
        cls.test_superuser_login_id = "22222222"
        cls.test_platform = "test_platform"
        cls.test_password = "Test_Password03"

        cls.superuser = AccountsModel.custom_objects.create_superuser(
            server_name=cls.test_servername,
            login_id=cls.test_superuser_login_id,
            platform=cls.test_platform,
            password=cls.test_password,
        )
        
        cls.user = AccountsModel.custom_objects.create_user(
            server_name=cls.test_servername,
            login_id=cls.test_user_login_id,
            platform=cls.test_platform,
            password=cls.test_password,
        )

    def test_user(self):
        self.assertIsNotNone(Test_add_user.user)
        user_id = str(Test_add_user.user)

        user = AccountsModel.custom_objects.get(account_id=str(Test_add_user.user))
        servername = user.get_servername()
        login_id = user.get_login_id()
        platform = user.get_platform()
        is_active = user.get_is_active()
        local_user_id = str(user)

        self.assertEqual(servername, Test_add_user.test_servername)
        self.assertEqual(login_id, Test_add_user.test_user_login_id)
        self.assertEqual(platform, Test_add_user.test_platform)
        self.assertEqual(is_active, False)
        self.assertEqual(user_id, local_user_id)
        self.assertIsNotNone(user.password)
        self.assertEqual(False, user.is_staff)

    
    def test_superuser(self):
        self.assertIsNotNone(self.superuser)
        superuser_id = str(Test_add_user.superuser)
        
        superuser = AccountsModel.custom_objects.get(account_id=str(Test_add_user.superuser))
        servername = superuser.get_servername()
        login_id = superuser.get_login_id()
        platform = superuser.get_platform()
        is_active = superuser.get_is_active()
        local_superuser_id = str(superuser)

        self.assertEqual(servername, Test_add_user.test_servername)
        self.assertEqual(login_id, Test_add_user.test_superuser_login_id)
        self.assertEqual(platform, Test_add_user.test_platform)
        self.assertEqual(is_active, True)
        self.assertEqual(superuser_id, local_superuser_id)
        self.assertIsNotNone(superuser.password)
        self.assertEqual(True, superuser.is_staff)


class Test_views(TestCase):

    def test_api_home_view(self):
        client = Client()
        response = client.get('/api/')
        self.assertEquals(response.status_code, 200)



class Test_api_endpoints():

    def test_view_accounts(self):
        url = reverse('mt5scheuler.accounts')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
