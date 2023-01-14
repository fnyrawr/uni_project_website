from django.shortcuts import render
from rest_framework import viewsets
from .models import Leaderboard
from .serializers import LeaderboardSerializer
from .forms import SearchForm


def leaderboard_list(request):
    all_entries = None
    entries_found = None
    search = False
    searchForm = SearchForm
    if request.method == "POST":
        search = True
        searchForm = SearchForm(request.POST)
        data = searchForm.data
        playername = data['playername']
        if playername:
            if playername:
                entries_found = Leaderboard.objects.filter(playername__contains=playername)
    else:
        all_entries = Leaderboard.objects.all()

    context = {'all_entries': all_entries,
               'entries_found': entries_found,
               'search': search,
               'form': searchForm, }
    return render(request, 'leaderboard-list.html', context)


class LeaderboardView(viewsets.ModelViewSet):
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        queryset = Leaderboard.objects.all()
        return queryset
