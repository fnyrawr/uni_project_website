from django.urls import path
from . import views

urlpatterns = [
    path('newquestion/', views.QuestionCreateView.as_view(), name='newquestion'),
    path('viewquestions/', views.question_list, name='viewquestions'),
    path('delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='deletequestion'),
]