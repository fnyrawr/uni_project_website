from django import forms
from .models import Survey, Question


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'review', 'wishes', 'gameidea', 'gamedesign', 'gameplay', 'websiteDesign']
        widgets = {
            'timestamp': forms.HiddenInput(),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category', 'question', 'timestamp']


class SurveySearchForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'review', 'wishes']


class QuestionSearchForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category']
