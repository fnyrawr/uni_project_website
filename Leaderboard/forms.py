from django import forms
from .models import Leaderboard

SORT_CHOICES = (
    ('PN', 'playername'),
    ('KC', 'killcount'),
    ('DD', 'damagedealt'),
    ('PT', 'playtime'),
    ('TM', 'time'),
    ('ID', 'id'),
)

class SearchForm(forms.ModelForm):
    sortby = forms.ChoiceField(choices = SORT_CHOICES)
    class Meta:
        model = Leaderboard
        fields = ['playername', 'sortby', 'mapname']
