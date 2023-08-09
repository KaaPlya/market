from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user


# Create your tests here.

class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data={
                'first_name': 'Murodjon',
                'username': 'murodjon',
                'email': 'aa@aa.aa',
                'password1': '12345',
                'password2': '12345',
            }
        )
        user = CustomUser.objects.get(username='murodjon')
        self.assertEqual(user.first_name, 'Murodjon')
        self.assertEqual(user.email, 'aa@aa.aa')
        self.assertTrue(user.check_password('Murod12345'))

        second_response = self.client.get("/users/profile/murodjon")
        self.assertEqual(second_response.status_code, 200)

        # login
        self.client.login(username='murodjon', password='murod12345')

        third_response = self.client.post(
            reverse('users:update'),
            data={
                'username': 'murodjon2',
                'first_name': 'Murodjon2',
                'last_name': 'Xudayberdiyev',
                'email': 'aaa@aaa.aaa',
                'phone_number': '+998942323',
                'tg_username': 'username',
            }
        )
        user = get_user(self.client)
        print(user.is_authenticated)
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.phone_number, '+998942323')
        self.assertEqual(user.first_name, 'Murodjon2')
        self.assertNotEqual(user.first_name, 'Murodjon')

