from django import forms
from .models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'review', 'wishes', 'gameidea', 'gamedesign', 'gameplay', 'websiteDesign']
        widgets = {
            'timestamp': forms.HiddenInput(),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['category', 'question', 'timestamp']
