from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from newsletter.models import Newsletter


class NewsletterViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.valid_data = {
            'email': 'test@example.com',
        }

    def test_newsletter_view_get(self):
        """GET request renders the newsletter form template"""
        response = self.client.get(reverse('newsletter'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/newsletter.html')
        self.assertContains(response, '<form')  # Basic form presence check

    def test_newsletter_form_valid_post(self):
        """Valid POST saves the form and sends an email"""
        response = self.client.post(reverse(
            'newsletter'), data=self.valid_data)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Newsletter.objects.count(), 1)
        self.assertEqual(
            Newsletter.objects.first().email, self.valid_data['email'])

        # Email sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(self.valid_data['email'], mail.outbox[0].to)

    def test_newsletter_form_invalid_post(self):
        """Invalid POST does not save or send email"""
        response = self.client.post(reverse('newsletter'), data={'email': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/newsletter.html')
        self.assertFormError(
            response, 'form', 'email', 'This field is required.')
        self.assertEqual(Newsletter.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)
