from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='rod',
            email='rod@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'rod')
        self.assertEqual(user.email, 'rod@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='clark',
            email='clark@dailyplanet.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'clark')
        self.assertEqual(admin_user.email, 'clark@dailyplanet.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
