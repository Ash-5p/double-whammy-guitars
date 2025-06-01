from django.test import TestCase
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from django.contrib.auth.models import User


class UserProfileFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='pass1234')

    def test_meta_model_and_exclude(self):
        form = UserProfileForm()
        self.assertEqual(form._meta.model, UserProfile)
        self.assertIn('user', form._meta.exclude)

    def test_placeholders_and_labels(self):
        form = UserProfileForm()
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County/State',
        }

        for field_name, placeholder in placeholders.items():
            self.assertIn('placeholder', form.fields[field_name].widget.attrs)
            self.assertTrue(
                form.fields[field_name].label is False or form.fields[
                    field_name].label == '')

        self.assertEqual(form.fields['default_country'].label, 'Country')

    def test_valid_form_data(self):
        form_data = {
            'default_phone_number': '123456789',
            'default_postcode': '12345',
            'default_town_or_city': 'Testville',
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Apt 4',
            'default_county': 'Test County',
            'default_country': 'GB',
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())
