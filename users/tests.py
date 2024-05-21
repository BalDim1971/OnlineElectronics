"""
Тесты для пользователя
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UsersTestCase(APITestCase):
    """
    Тестируем пользователя.
    """
    def setUp(self) -> None:
        """
        Суперпользователь admin и один тестовый для удаления/обновления
        """
        self.user = User(email='admin@sky.pro',
                         first_name='Admin',
                         last_name='SkyPro',
                         is_superuser=True,
                         is_staff=True,
                         is_active=True,
                         )
        self.user.set_password('admin')
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {"email": "admin@sky.pro", "password": "admin"}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}

        self.test_user = User(
            email="test@sky.pro",
            is_superuser=False,
            is_staff=True,
            is_active=True,
            password="test1234",
        )
        self.test_user.save()

    def test_create_user(self):
        """
        Тест операции создания (create) пользователя
        """
        data = {
            "email": "test1@test.ru",
            "is_superuser": False,
            "is_staff": False,
            "is_active": True,
            "password": "123456789",
        }
        create_user = reverse('users:users_create')
        response = self.client.post(create_user, data,
                                    format="json", **self.headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], data['email'])

    def test_retrieve_user(self):
        """
        Тест операции чтения (retrieve) пользователя
        """
        retrieve_url = reverse('users:users_view',
                               args=[self.user.id])
        response = self.client.get(retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_delete_user(self):
        """
        Тест операции удаления (delete) пользователя
        """
        delete_url = reverse('users:users_delete',
                             args=[self.test_user.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(id=self.test_user.id).exists())

    def test_list_user(self):
        """
        Тест операции получения списка пользователя
        """
        list_url = reverse('users:users_list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)

    def test_str_user(self):
        """
        Тест проверки получения строки...
        """
        my_str = str(self.user)
        self.assertEqual(my_str, "admin@sky.pro")
