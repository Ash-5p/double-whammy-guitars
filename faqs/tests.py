from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from faqs.models import FAQ


class FAQViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.faq = FAQ.objects.create(
            question="Test question?",
            answer="Test answer."
        )
        self.superuser = User.objects.create_superuser(
            username='admin', email='admin@test.com', password='password123'
        )
        self.user = User.objects.create_user(
            username='regular', email='user@test.com', password='password123'
        )
        self.valid_data = {
            'question': 'New FAQ?',
            'answer': 'New answer.'
        }

    def test_view_faqs_get_as_anonymous_user(self):
        """GET faqs page as anonymous should succeed."""
        response = self.client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faqs.html')

    def test_add_faq_post_as_non_superuser(self):
        """POST to add FAQ as non-superuser redirects with error."""
        self.client.login(username='regular', password='password123')
        response = self.client.post(reverse('faqs'), data=self.valid_data)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(FAQ.objects.count(), 1)

    def test_add_faq_post_as_superuser(self):
        """POST to add FAQ as superuser creates new FAQ."""
        self.client.login(username='admin', password='password123')
        response = self.client.post(reverse('faqs'), data=self.valid_data)
        self.assertRedirects(response, reverse('faqs'))
        self.assertEqual(FAQ.objects.count(), 2)

    def test_edit_faq_as_superuser(self):
        """Superuser can edit an FAQ."""
        self.client.login(username='admin', password='password123')
        url = reverse('edit_faq', args=[self.faq.id])
        response = self.client.post(url, {
            'question': 'Updated?', 'answer': 'Updated answer.'})
        self.assertRedirects(response, reverse('faqs'))
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question, 'Updated?')

    def test_edit_faq_as_non_superuser(self):
        """Non-superuser is redirected when trying to edit an FAQ."""
        self.client.login(username='regular', password='password123')
        url = reverse('edit_faq', args=[self.faq.id])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('home'))

    def test_delete_faq_as_superuser(self):
        """Superuser can delete an FAQ."""
        self.client.login(username='admin', password='password123')
        response = self.client.post(reverse('delete_faq', args=[self.faq.id]))
        self.assertRedirects(response, reverse('faqs'))
        self.assertFalse(FAQ.objects.filter(pk=self.faq.id).exists())

    def test_delete_faq_as_non_superuser(self):
        """Non-superuser cannot delete an FAQ."""
        self.client.login(username='regular', password='password123')
        response = self.client.post(reverse('delete_faq', args=[self.faq.id]))
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(FAQ.objects.filter(pk=self.faq.id).exists())
