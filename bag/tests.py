from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class BagViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='A test product'
        )
        self.item_id = str(self.product.id)
        self.redirect_url = reverse('view_bag')

    def test_view_bag_page_renders(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_new_item(self):
        response = self.client.post(reverse(
            'add_to_bag', args=[self.item_id]), {
            'quantity': 2,
            'redirect_url': self.redirect_url
        })
        session = self.client.session
        self.assertEqual(session['bag'][self.item_id], 2)
        self.assertRedirects(response, self.redirect_url)

    def test_add_to_bag_existing_item(self):
        session = self.client.session
        session['bag'] = {self.item_id: 1}
        session.save()
        response = self.client.post(reverse(
            'add_to_bag', args=[self.item_id]), {
            'quantity': 3,
            'redirect_url': self.redirect_url
        })
        session = self.client.session
        self.assertEqual(session['bag'][self.item_id], 4)

    def test_adjust_bag_quantity(self):
        session = self.client.session
        session['bag'] = {self.item_id: 2}
        session.save()
        response = self.client.post(reverse(
            'adjust_bag', args=[self.item_id]), {
            'quantity': 5
        })
        session = self.client.session
        self.assertEqual(session['bag'][self.item_id], 5)
        self.assertRedirects(response, reverse('view_bag'))

    def test_adjust_bag_to_zero_removes_item(self):
        session = self.client.session
        session['bag'] = {self.item_id: 2}
        session.save()
        response = self.client.post(reverse(
            'adjust_bag', args=[self.item_id]), {
            'quantity': 0
        })
        session = self.client.session
        self.assertNotIn(self.item_id, session['bag'])
        self.assertRedirects(response, reverse('view_bag'))

    def test_remove_from_bag(self):
        session = self.client.session
        session['bag'] = {self.item_id: 2}
        session.save()
        response = self.client.post(reverse(
            'remove_from_bag', args=[self.item_id]))
        session = self.client.session
        self.assertNotIn(self.item_id, session['bag'])
        self.assertEqual(response.status_code, 200)

    def test_remove_from_bag_error_handling(self):
        response = self.client.post(reverse(
            'remove_from_bag', args=[self.item_id]))
        self.assertEqual(response.status_code, 500)
