from rest_framework import serializers

from dashboard.models import DataEvent, DataPipeline

class DataEventSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = DataEvent
        fields = ('user', 'pipeline', 'json_data',)    
