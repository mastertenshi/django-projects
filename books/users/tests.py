from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def setUp(self):
        self.User = get_user_model()


    def test_create_user(self):
        user = self.User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')

        self.assertTrue(user.is_active)

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username='super',
            email='super@email.com',
            password='testpass123',
        )
        self.assertEqual(admin_user.username, 'super')
        self.assertEqual(admin_user.email, 'super@email.com')

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
