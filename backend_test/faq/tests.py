from django.test import TestCase
from .models import FAQ
from googletrans import Translator

class FAQModelTest(TestCase):

    def test_faq_creation(self):
        # Create a new FAQ object
        faq = FAQ.objects.create(
            question="What is Django?", 
            answer="<p>Django is a web framework.</p>"
        )
        
        # Check if the FAQ object was created
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "<p>Django is a web framework.</p>")
        self.assertTrue(faq.pk)  # Check if the FAQ object has been saved to the database

    def test_translation_on_save(self):
        # Create a new FAQ object without translations
        faq = FAQ.objects.create(
            question="What is Django?", 
            answer="<p>Django is a web framework.</p>"
        )
        
        # Check if translations were done correctly on save
        self.assertIsNotNone(faq.translated_question_hi)
        self.assertIsNotNone(faq.translated_question_bn)
        self.assertNotEqual(faq.translated_question_hi, faq.question)
        self.assertNotEqual(faq.translated_question_bn, faq.question)

    def test_get_translated_question(self):
        # Create a FAQ object with some translations
        faq = FAQ.objects.create(
            question="What is Django?", 
            answer="<p>Django is a web framework.</p>",
            translated_question_hi="Django kya hai?",
            translated_question_bn="Django ki holo?"
        )
        
        # Test 'hi' translation
        translated_hi = faq.get_translated_question('hi')
        self.assertEqual(translated_hi, "Django kya hai?")
        
        # Test 'bn' translation
        translated_bn = faq.get_translated_question('bn')
        self.assertEqual(translated_bn, "Django ki holo?")
        
        # Test default (original) question
        translated_default = faq.get_translated_question('en')
        self.assertEqual(translated_default, "What is Django?")

    def test_translation_not_null_on_create(self):
        # Create a FAQ object with only a question and answer
        faq = FAQ.objects.create(
            question="What is Python?", 
            answer="<p>Python is a programming language.</p>"
        )
        
        # Check if both translated questions are not null after saving
        self.assertIsNotNone(faq.translated_question_hi)
        self.assertIsNotNone(faq.translated_question_bn)
