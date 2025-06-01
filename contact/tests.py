from django.test import TestCase
from django.conf import settings
from unittest.mock import patch
from contact.models import Contact
from contact.views import send_confirmation_email


class ContactEmailTests(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name='Test User',
            email='test@example.com',
            message='Just testing'
        )

    @patch('contact.views.send_mail')
    @patch('contact.views.render_to_string')
    def test_send_confirmation_email(self, mock_render_to_string,
                                     mock_send_mail):
        mock_render_to_string.side_effect = ['Test Subject\n', 'Test Body']
        send_confirmation_email(self.contact)

        mock_render_to_string.assert_any_call(
            'contact/confirmation_emails/confirmation_email_subject.txt',
            {'contact': self.contact}
        )
        mock_render_to_string.assert_any_call(
            'contact/confirmation_emails/confirmation_email_body.txt',
            {'contact': self.contact}
        )
        mock_send_mail.assert_called_once_with(
            'Test Subject',
            'Test Body',
            settings.DEFAULT_FROM_EMAIL,
            [self.contact.email]
        )
