from django.urls import path
from .views import FAQListCreate, FAQDetail, AISuggestAnswer


urlpatterns = [
path('faqs/', FAQListCreate.as_view()),
path('faqs/<int:id>/', FAQDetail.as_view()),
path('ai/suggest-answer/', AISuggestAnswer.as_view())
]