from django.shortcuts import render
from django.views.generic import ListView
from .models import Team
# Create your views here.

# class TeamListView(ListView):
#     model = Team

def index(request):
    return render(request, "core/home.html")

def team(request):
    team_list = Team.objects.all()
    context = {'team_list': team_list}
    return render(request, "core/team.html", context)