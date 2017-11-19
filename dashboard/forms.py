from django import forms
from .models import Chart, Dashboard, DataPipeline, DataPointType

class ChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ['name', 'team', 'dataPointInfo', 'positionID', 'graphType']

    def __init__(self, *args, **kwargs):
        super(ChartForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ["name", "team", "pipeline", "charts"]

    def __init__(self, *args, **kwargs):
        super(DashboardForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PipelineForm(forms.ModelForm):
    class Meta:
        model = DataPipeline
        fields = ['name', 'team']

    def __init__(self, *args, **kwargs):
        super(PipelineForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 

class DataPointTypeForm(forms.ModelForm):
    class Meta:
        model = DataPointType
        fields = ['name', 'pipeline', 'dataType']

    def __init__(self, *args, **kwargs):
        super(DataPointTypeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 