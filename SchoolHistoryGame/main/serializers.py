from rest_framework import serializers
from .models import HistoryList

class HistoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoryList
        fields = ['date', 'text']
