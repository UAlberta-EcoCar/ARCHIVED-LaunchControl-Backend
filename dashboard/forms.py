from django import forms
from .models import Chart, Dashboard

class ChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ['name', 'team', 'dataPointInfo', 'positionID', 'graphType']

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ["name", "team", "pipeline", "charts"]