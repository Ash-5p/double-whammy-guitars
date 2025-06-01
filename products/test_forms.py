from django.test import TestCase
from products.forms import ProductForm
from products.models import Category, Subcategory, Brand


class ProductFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="electronics", friendly_name="Electronics")
        self.subcategory = Subcategory.objects.create(
            name="phones", friendly_name="Phones")
        self.brand = Brand.objects.create(name="Acme", friendly_name="ACME")

    def test_form_category_choices_are_friendly_names(self):
        form = ProductForm()
        category_choices = form.fields['category'].choices
        self.assertIn((self.category.id, "Electronics"), category_choices)

    def test_form_subcategory_choices_are_friendly_names(self):
        form = ProductForm()
        subcategory_choices = form.fields['subcategory'].choices
        self.assertIn((self.subcategory.id, "Phones"), subcategory_choices)

    def test_form_brand_choices_are_friendly_names(self):
        form = ProductForm()
        brand_choices = form.fields['brand'].choices
        self.assertIn((self.brand.id, "ACME"), brand_choices)

    def test_valid_form_data(self):
        form_data = {
            'name': 'Test Product',
            'description': 'A cool test product.',
            'price': 99.99,
            'category': self.category.id,
            'subcategory': self.subcategory.id,
            'brand': self.brand.id,
            'has_sizes': False,
            'sku': 'TP123',
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())
