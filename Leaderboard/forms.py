from django import forms
from .models import Leaderboard


class SearchForm(forms.ModelForm):
    class Meta:
        model = Leaderboard
        fields = ['playername']