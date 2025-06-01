from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Category, Subcategory


class ProductViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create categories and subcategories
        self.category = Category.objects.create(
            name="Clothing", friendly_name="Clothing")
        self.subcategory = Subcategory.objects.create(
            name="Shirts", friendly_name="Shirts")

        # Create sample product
        self.product = Product.objects.create(
            name="Test Product",
            description="A product for testing.",
            price=19.99,
            category=self.category,
            subcategory=self.subcategory,
        )

        # Create a superuser
        self.superuser = User.objects.create_superuser(
            username='admin', email='admin@test.com', password='password'
        )

        # Regular user
        self.user = User.objects.create_user(
            username='user', email='user@test.com', password='password'
        )

    def test_all_products_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertContains(response, self.product.name)

    def test_all_products_view_search(self):
        response = self.client.get(reverse('products'), {'q': 'Test'})
        self.assertContains(response, 'Test Product')

    def test_product_detail_view(self):
        response = self.client.get(reverse(
            'product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, self.product.name)

    def test_product_detail_view_invalid_id(self):
        response = self.client.get(reverse('product_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_add_product_view_superuser(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)

        # POST with valid data
        response = self.client.post(reverse('add_product'), {
            'name': 'New Product',
            'description': 'Test add',
            'price': 10.00,
            'category': self.category.id,
            'subcategory': self.subcategory.id
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name='New Product').exists())

    def test_add_product_view_non_superuser(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('add_product'))
        self.assertRedirects(response, reverse('home'))

    def test_edit_product_view_superuser(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse(
            'edit_product', args=[self.product.id]), {
            'name': 'Edited Name',
            'description': self.product.description,
            'price': self.product.price,
            'category': self.category.id,
            'subcategory': self.subcategory.id
        }, follow=True)
        self.assertRedirects(response, reverse(
            'product_detail', args=[self.product.id]))
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Edited Name')

    def test_edit_product_view_non_superuser(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('home'))

    def test_delete_product_view_superuser(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse(
            'delete_product', args=[self.product.id]), follow=True)
        self.assertRedirects(response, reverse('products'))
        self.assertFalse(Product.objects.filter(pk=self.product.id).exists())

    def test_delete_product_view_non_superuser(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse(
            'delete_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Product.objects.filter(pk=self.product.id).exists())
