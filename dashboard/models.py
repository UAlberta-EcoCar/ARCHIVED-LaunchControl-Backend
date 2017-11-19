from django.db import models
from django.contrib.auth.models import User

import jsonfield 

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=80, unique=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class DataPipeline(models.Model):
    name = models.CharField(max_length=80)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DataPointType(models.Model):
    NUMBER = 'number'
    STRING = 'string'
    BOOLEAN = 'boolean'
    LAUNCH_CONTROL_DATA_TYPES = (
        (NUMBER, 'Number'),
        (STRING, 'String'),
        (BOOLEAN, 'Boolean'),
    )
    name = models.CharField(max_length=50)
    pipeline = models.ForeignKey(DataPipeline, on_delete=models.CASCADE)
    dataType = models.CharField(
        max_length=20,
        choices=LAUNCH_CONTROL_DATA_TYPES,
        default=NUMBER,
    )

    def __str__(self):
        return self.name

class DataEvent(models.Model):
    user = models.ForeignKey(User)
    pipeline = models.ForeignKey(DataPipeline, on_delete=models.CASCADE)
    json_data = jsonfield.JSONField()
    time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk


class Chart(models.Model):
    LINECHART = 'linechart'
    LAUNCH_CONTROL_CHART_TYPES = (
        (LINECHART, 'Line Chart'),
    )
    name = models.CharField(max_length=80)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    dataPointInfo = models.ForeignKey(DataPointType, on_delete=models.CASCADE)
    positionID = models.IntegerField()
    graphType = models.CharField(
        max_length=20,
        choices=LAUNCH_CONTROL_CHART_TYPES,
        default=LINECHART,
    )

    def __str__(self):
        return self.name


class Dashboard(models.Model):
    name = models.CharField(max_length=80)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    pipeline = models.ForeignKey(DataPipeline, on_delete=models.CASCADE)
    charts = models.ManyToManyField(Chart, blank=True)

    def __str__(self):
        return self.name
