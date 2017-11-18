from django.contrib import admin

from .models import Team, DataPipeline, DataPointType, DataEvent, Dashboard, Chart

admin.site.register(Team)
admin.site.register(DataPipeline)
admin.site.register(DataPointType)
admin.site.register(DataEvent)
admin.site.register(Dashboard)
admin.site.register(Chart)
