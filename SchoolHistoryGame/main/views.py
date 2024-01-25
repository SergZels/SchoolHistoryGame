from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoryList,Subtopics,SubtopicsContent,MainContent
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import HistoryListSerializers,SubtopicsSerializers,SubtopicsContentsSerializers,MainContentsSerializers
def index(request):
    queryset = HistoryList.objects.all()
    data = list(queryset.values())
    return JsonResponse(data, safe=False)

def load(request):
    return render(request, "load.html",)

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = HistoryList.objects.all()
    serializer_class = HistoryListSerializers
    permission_classes = [permissions.AllowAny]

class SubtopicsViewSet(viewsets.ModelViewSet):
    serializer_class = SubtopicsSerializers
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        id = self.kwargs['id']  # Отримуємо id з URL
        return Subtopics.objects.filter(history_list=id)
       # return Subtopics.objects.all()

class SubtopicsContentViewSet(viewsets.ModelViewSet):
    serializer_class = SubtopicsContentsSerializers
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        id = self.kwargs['id']  # Отримуємо id з URL
        return SubtopicsContent.objects.filter(subtopics=id)

class MainContentViewSet(viewsets.ModelViewSet):
    serializer_class = MainContentsSerializers
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        id = self.kwargs['id']  # Отримуємо id з URL
        return MainContent.objects.filter(history_list=id)