from django.urls import path
from . import views

urlpatterns = [
    path('newquestion/', views.QuestionCreateView.as_view(), name='newquestion'),
    path('viewquestions/', views.question_list, name='viewquestions'),
    path('deletequestion/<int:pk>/', views.QuestionDeleteView.as_view(), name='deletequestion'),
    path('newsurvey/', views.SurveyCreateView.as_view(), name='newsurvey'),
    path('viewsurveys/', views.survey_list, name='viewsurveys'),
    path('reviewswishes/', views.reviews_wishes_list, name='viewreviewswishes'),
    path('statistics/', views.statistics_diagrams, name='statistics'),
    path('deletesurvey/<int:pk>/', views.SurveyDeleteView.as_view(), name='deletesurvey'),
]