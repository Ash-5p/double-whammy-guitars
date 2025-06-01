from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'message': 'Hello, I have a question about your service.'
        }

    def test_form_has_correct_fields(self):
        form = ContactForm()
        expected_fields = ['name', 'email', 'message']
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_form_valid_data(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_name(self):
        data = self.valid_data.copy()
        data['name'] = ''
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_form_missing_email(self):
        data = self.valid_data.copy()
        data['email'] = ''
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_missing_message(self):
        data = self.valid_data.copy()
        data['message'] = ''
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)

    def test_form_invalid_email_format(self):
        data = self.valid_data.copy()
        data['email'] = 'invalid-email'
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
