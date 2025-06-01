from django.test import TestCase
from newsletter.forms import NewsletterForm


class NewsletterFormTests(TestCase):

    def test_form_has_only_email_field(self):
        form = NewsletterForm()
        self.assertEqual(list(form.fields.keys()), ['email'])

    def test_form_accepts_valid_email(self):
        form = NewsletterForm(data={'email': 'test@example.com'})
        self.assertTrue(form.is_valid())

    def test_form_rejects_empty_email(self):
        form = NewsletterForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_rejects_invalid_email(self):
        form = NewsletterForm(data={'email': 'not-an-email'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
