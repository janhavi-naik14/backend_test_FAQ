# urls.py
from django.urls import path
from .views import FAQListCreateView, FAQDetailView

urlpatterns = [
    path('faq/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('faq/<int:id>/', FAQDetailView.as_view(), name='faq-detail'),
]