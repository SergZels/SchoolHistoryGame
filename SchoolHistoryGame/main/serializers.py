from rest_framework import serializers
from .models import HistoryList,Subtopics,SubtopicsContent,MainContent

class HistoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoryList
        fields = ['pk','date', 'text']

class SubtopicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subtopics
        fields = ['history_list','pk','title']

class SubtopicsContentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubtopicsContent
        fields = ['type','text','subtopics']

class MainContentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = ['type','text','history_list']