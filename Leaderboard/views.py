from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from rest_framework import viewsets
from .models import Leaderboard
from .serializers import LeaderboardSerializer
from .forms import SearchForm


def leaderboard_list(request):
    all_entries = None
    entries_found = None
    search = False
    searchForm = SearchForm
    data = None
    mapname = 'Space'
    if request.method == "POST":
        search = True
        searchForm = SearchForm(request.POST)
        data = searchForm.data
        if data['mapname']:
            mapname = data['mapname']
        playername = data['playername']
        entries_found = Leaderboard.objects.filter(mapname__contains=mapname).order_by('playtime')

        if playername:
            entries_found = entries_found.filter(playername__contains=playername)
        if data['sortby'] == 'PN':
            entries_found = entries_found.order_by('playername')
        if data['sortby'] == 'KC':
            entries_found = entries_found.order_by('-killcount')
        if data['sortby'] == 'DD':
            entries_found = entries_found.order_by('-damagedealt')
        if data['sortby'] == 'TM':
            entries_found = entries_found.order_by('-time')
        if data['sortby'] == 'PT':
            entries_found = entries_found.order_by('playtime')
        if data['sortby'] == 'ID':
            entries_found = entries_found.order_by('id')
    else:
        all_entries = Leaderboard.objects.filter(mapname__contains=mapname).order_by('playtime')

    context = {'all_entries': all_entries,
               'entries_found': entries_found,
               'search': search,
               'form': searchForm,
               'data': data,
               }
    return render(request, 'leaderboard-list.html', context)


class LeaderboardView(viewsets.ModelViewSet):
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        queryset = Leaderboard.objects.order_by('-playtime')
        return queryset


class LeaderboardDeleteView(DeleteView):
    model = Leaderboard
    context_object_name = 'that_one_entry'
    success_url = reverse_lazy('leaderboard-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, **kwargs):
        entry_id = kwargs['pk']
        entry = Leaderboard.objects.get(id=entry_id)
        mapname = entry.mapname
        entry.delete()
        data = {'mapname': mapname, 'playername': None, 'sortby': None}
        all_entries = Leaderboard.objects.filter(mapname__contains=mapname).order_by('playtime')
        context = {'all_entries': all_entries,
                   'entries_found': None,
                   'search': False,
                   'form': SearchForm,
                   'data': data,
                   }
        return render(request, 'leaderboard-list.html', context)
