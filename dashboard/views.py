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
            form.save_m2m()
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
    data['charts'] = dashboard_to_view.charts.all()
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
            form.save_m2m()
            return redirect('dashboard', pk=dboard.pk)
    else:
        form = DashboardForm(instance=dboard)
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data = {}
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    data['form'] = form
    return render(request, 'dashboard/dashboard_edit.html', data)

def chart(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    chart_to_view = get_object_or_404(Chart, pk=pk)
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data = {}
    data['chart'] = chart_to_view
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    return render(request, "dashboard/dashboard_chart_view.html", data)

def chart_edit(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    curr_chart = get_object_or_404(Chart, pk=pk)
    if request.method == "POST":
        form = ChartForm(request.POST, instance=curr_chart)
        if form.is_valid():
            curr_chart = form.save(commit=False)
            curr_chart.save()
            return redirect('chart', pk=curr_chart.pk)
    else:
        form = ChartForm(instance=curr_chart)
    return render(request, 'dashboard/dashboard_edit_chart.html', {'form': form})

def pipeline(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    pipeline_to_view = get_object_or_404(DataPipeline, pk=pk)
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data = {}
    data['pipeline'] = pipeline_to_view
    data['dashboards'] = dashboards
    data['pipelines'] = pipelines
    return render(request, "dashboard/dashboard_pipeline_view.html", data)

def pipeline_edit(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    curr_pipeline = get_object_or_404(DataPipeline, pk=pk)
    if request.method == "POST":
        form = DataPipelineForm(request.POST, instance=curr_pipeline)
        if form.is_valid():
            curr_pipeline = form.save(commit=False)
            curr_pipeline.save()
            form.save_m2m()
            return redirect('pipeline', pk=curr_pipeline.pk)
    else:
        form = PipelineForm(instance=curr_pipeline)
    dashboards = Dashboard.objects.filter(team__in=request.user.userprofile.team.all())
    pipelines = DataPipeline.objects.filter(team__in=request.user.userprofile.team.all())
    data = {}
    data['pipeline'] = pipeline_to_view
    data['dashboards'] = dashboards
    data['form'] = form
    return render(request, 'dashboard/dashboard_edit_pipeline.html', {'form': form})

def datapointtype(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    datapointtype_to_view = get_object_or_404(DataPointType, pk=pk)
    data = {}
    data['datapointtype'] = datapointtype_to_view
    return render(request, "dashboard/dashboard_datapointtype_view.html", data)

def datapointtype_edit(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    curr_datapointtype = get_object_or_404(DataPointType, pk=pk)
    if request.method == "POST":
        form = DataPointTypeForm(request.POST, instance=curr_datapointtype)
        if form.is_valid():
            curr_datapointtype = form.save(commit=False)
            curr_datapointtype.save()
            return redirect('datapointtype', pk=curr_datapointtype.pk)
    else:
        form = DataPointTypeForm(instance=curr_datapointtype)
    return render(request, 'dashboard/dashboard_edit_datapointtype.html', {'form': form})