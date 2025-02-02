# models.py
from django.db import models
from googletrans import Translator
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    translated_question_hi = models.TextField(blank=True, null=True)
    translated_question_bn = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        if lang == 'hi':
            return self.translated_question_hi if self.translated_question_hi else self.question
        elif lang == 'bn':
            return self.translated_question_bn if self.translated_question_bn else self.question
        return self.question  # Default to original question

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.translated_question_hi:
            self.translated_question_hi = translator.translate(self.question, dest='hi').text
        if not self.translated_question_bn:
            self.translated_question_bn = translator.translate(self.question, dest='bn').text
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50]