from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoryList
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import HistoryListSerializers
def index(request):
    queryset = HistoryList.objects.all()
    data = list(queryset.values())
    return JsonResponse(data, safe=False)


class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HistoryList.objects.all()
    serializer_class = HistoryListSerializers
    permission_classes = [permissions.AllowAny]