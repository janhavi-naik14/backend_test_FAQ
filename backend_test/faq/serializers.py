# serializers.py
from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'answer']

    def get_translated_question(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'all')
        if lang in ['hi', 'bn']:
            return obj.get_translated_question(lang)
        return {
            'question_en': obj.question,
            'question_hi': obj.translated_question_hi,
            'question_bn': obj.translated_question_bn,
        }
