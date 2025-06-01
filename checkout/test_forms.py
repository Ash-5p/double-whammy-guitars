from django.test import TestCase
from checkout.forms import OrderForm


class OrderFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '0123456789',
            'street_address1': '123 Test St',
            'street_address2': '',
            'town_or_city': 'Testville',
            'postcode': 'AB1 2CD',
            'country': 'GB',
            'county': 'Testshire',
        }

    def test_form_has_correct_fields(self):
        form = OrderForm()
        expected_fields = [
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country', 'county'
        ]
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_form_placeholders_and_css_classes(self):
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs['placeholder'],
            'Full Name *'
        )
        self.assertIn('stripe-style-input',
                      form.fields['full_name'].widget.attrs['class'])
        self.assertFalse(form.fields['full_name'].label)

        self.assertEqual(
            form.fields['street_address2'].widget.attrs['placeholder'],
            'Street Address 2'
        )

    def test_country_field_label_and_attrs(self):
        form = OrderForm()
        country_field = form.fields['country']
        self.assertEqual(country_field.label, 'Country')
        self.assertIn('required', country_field.widget.attrs)
        self.assertIn('form-control', country_field.widget.attrs['class'])

    def test_valid_form_submission(self):
        form = OrderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_required_fields(self):
        invalid_data = self.valid_data.copy()
        invalid_data.pop('full_name')
        form = OrderForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
