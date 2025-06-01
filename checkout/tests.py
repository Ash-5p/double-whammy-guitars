from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from products.models import Product


class CheckoutViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.product = Product.objects.create(
            name='Test Product', price=10.00, description='Test product')
        self.item_id = str(self.product.id)
        self.bag = {self.item_id: 2}
        session = self.client.session
        session['bag'] = self.bag
        session.save()

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_modify):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('cache_checkout_data'), {
            'client_secret': 'pi_12345_secret_abc',
            'save_info': True
        })
        self.assertEqual(response.status_code, 200)
        mock_modify.assert_called_once()

    @patch('checkout.views.stripe.PaymentIntent.modify', side_effect=Exception('Stripe error'))
    def test_cache_checkout_data_failure(self, mock_modify):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('cache_checkout_data'), {
            'client_secret': 'pi_12345_secret_abc',
            'save_info': True
        })
        self.assertEqual(response.status_code, 400)

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_get_no_bag(self, mock_create_intent):
        session = self.client.session
        session['bag'] = {}
        session.save()
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, reverse('products'))
