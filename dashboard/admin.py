from django.contrib import admin

from .models import Team, DataPipeline, DataPointType, DataEvent, Dashboard, Chart

class DataEventAdmin(admin.ModelAdmin):
    search_fields = ('pk',)
    list_display = ('pk', 'user', 'pipeline', 'json_data',)

admin.site.register(Team)
admin.site.register(DataPipeline)
admin.site.register(DataPointType)
admin.site.register(DataEvent, DataEventAdmin)
admin.site.register(Dashboard)
admin.site.register(Chart)
