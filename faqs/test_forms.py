from django.test import TestCase
from faqs.forms import FAQForm


class FAQFormTests(TestCase):

    def setUp(self):
        self.valid_data = {
            'question': 'What is your return policy?',
            'answer': 'You can return any item within 30 days.'
        }

    def test_form_has_correct_fields(self):
        form = FAQForm()
        self.assertEqual(list(form.fields.keys()), ['question', 'answer'])

    def test_form_accepts_valid_data(self):
        form = FAQForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_question(self):
        data = self.valid_data.copy()
        data['question'] = ''
        form = FAQForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors)

    def test_form_missing_answer(self):
        data = self.valid_data.copy()
        data['answer'] = ''
        form = FAQForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('answer', form.errors)
