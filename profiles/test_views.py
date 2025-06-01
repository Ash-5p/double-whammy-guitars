from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order


class ProfileViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create user and associated profile
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com', password='password123'
        )
        self.profile = UserProfile.objects.get(user=self.user)

        # Create a dummy order
        self.order = Order.objects.create(
            order_number='ORD123456',
            user_profile=self.profile,
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='GB',
            postcode='AB1 2CD',
            town_or_city='Testville',
            street_address1='123 Test St',
            street_address2='',
            county='Testshire',
        )

    def test_profile_view_get(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIn('form', response.context)
        self.assertIn('orders', response.context)
        self.assertTrue(response.context['on_profile_page'])

    def test_profile_view_post_valid(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('profile'), {
            'default_phone_number': '9999999999',
            'default_country': 'GB',
            'default_postcode': 'ZZ1 1ZZ',
            'default_town_or_city': 'New Town',
            'default_street_address1': '1 New St',
            'default_street_address2': '',
            'default_county': 'New County',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '9999999999')
        self.assertContains(response, 'Profile updated successfully')

    def test_order_history_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse(
            'order_history', args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, self.order.order_number)
        self.assertTrue(response.context['from_profile'])

    def test_order_history_404_for_invalid_order(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('order_history', args=['INVALID']))
        self.assertEqual(response.status_code, 404)
