from django.shortcuts import render

from django.http import Http404
# Create your views here.

def dashboard_home(request):
    if not request.user.is_authenticated:
        raise Http404
    data = {}
    return render(request, "dashboard/dashboard_index.html", data)

def pipeline_home(request):
    if not request.user.is_authenticated:
        raise Http404
    pipelines = DataPipeline.objects.filter(team=request.user.userprofile.team)
    data = {}
    data[pipelines] = pipelines
    return render(request, "dashboard/pipeline_home.html", data)
