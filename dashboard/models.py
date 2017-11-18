from django.db import models
from django.contrib.auth.models import User

import jsonfield 

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=80, unique=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class DataPipeline(models.Model):
    name = models.CharField(max_length=80)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

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

class DataEvent(models.Model):
    user = models.ForeignKey(User)
    pipeline = models.ForeignKey(DataPipeline, on_delete=models.CASCADE)
    json_data = jsonfield.JSONField()
    time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
