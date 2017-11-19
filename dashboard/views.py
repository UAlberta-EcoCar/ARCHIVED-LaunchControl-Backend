from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import DataPipeline, Chart, Dashboard, DataPointType
from .forms import ChartForm, DashboardForm, PipelineForm, DataPointTypeForm 
from django import forms
from rest_framework.authtoken.models import Token
# Create your views here.

def dashboard_home(request):
    if not request.user.is_authenticated:
        raise Http404
    data = {}
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    return render(request, "dashboard/dashboard_index.html", data)

def pipeline_home(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    datapipeline_to_view = get_object_or_404(DataPipeline, pk=pk)
    data = {}
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    datapoints = DataPointType.objects.filter(pipeline=datapipeline_to_view)
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    data['datapipeline'] = datapipeline_to_view
    data['datapoints'] = datapoints
    return render(request, "dashboard/dashboard_pipeline.html", data)

def new_chart(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        form = ChartForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('dashboard_home')
    else:
        form = ChartForm()

    return render(request, "dashboard/dashboard_new_chart.html", {'form': form})

def new_dashboard(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('dashboard_home')
    else:
        form = DashboardForm()

    return render(request, "dashboard/dashboard_new_dashboard.html", {'form': form})

def new_pipeline(request): #####
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        form = PipelineForm(request.POST) #####
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('dashboard_home')
    else:
        form = PipelineForm()

    return render(request, "dashboard/dashboard_new_pipeline.html", {'form': form}) ####

def new_datapointtype(request): #####
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        form = DataPointTypeForm(request.POST) 
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('dashboard_home')
    else:
        form = DataPointTypeForm()

    return render(request, "dashboard/dashboard_new_datapointtype.html", {'form': form}) ####

def dashboard(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    dashboard_to_view = get_object_or_404(Dashboard, pk=pk)
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data = {}
    data['dashboard_to_view'] = dashboard_to_view
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    return render(request, "dashboard/dashboard_view.html", data)

def api_dashboard(request):
    if not request.user.is_authenticated:
        raise Http404
    api_token, created = Token.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            api_token.delete()
            api_token = Token.objects.create(user=request.user)
            return redirect('api_dashboard')
    else:
        form = forms.Form()
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data = {}
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    data['api_token'] = api_token
    data['form'] = form
    return render(request, "dashboard/dashboard_api.html", data)

def dashboard_edit(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    dboard = get_object_or_404(Dashboard, pk=pk)
    if request.method == "POST":
        form = DashboardForm(request.POST, instance=dboard)
        if form.is_valid():
            dboard = form.save(commit=False)
            dboard.save()
            return redirect('dashboard', pk=dboard.pk)
    else:
        form = DashboardForm(instance=dboard)
    return render(request, 'dashboard/dashboard_edit.html', {'form': form})