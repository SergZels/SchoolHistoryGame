from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoryList

def index(request):
    queryset = HistoryList.objects.all()
    data = list(queryset.values())
    return JsonResponse(data, safe=False)