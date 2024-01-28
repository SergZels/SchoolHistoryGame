from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoryList,Subtopics,SubtopicsContent,MainContent
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .serializers import HistoryListSerializers,SubtopicsSerializers,SubtopicsContentsSerializers,MainContentsSerializers
import logging
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)
loggerINFO = logging.getLogger('django2')
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

 #   @method_decorator(cache_page(60))  # кешує на 60 секунд
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_queryset(self):
        loggerINFO.info(f'{datetime.now()} MainContentViewSet ')
        id = self.kwargs['id']  # Отримуємо id з URL
        # cache.set('my_key', 'my_value', timeout=3600)
        #
        # value = cache.get('my_key')
        #
        # if value is not None:
        #     print(value)

        return MainContent.objects.filter(history_list=id)



# class SubtContALL(APIView):
#     def get(self,request,id):
#         lst = Subtopics.objects.filter(history_list=id).values()
#         return Response({'subtopics':list(lst)})
class SubtopicWithContent(APIView):
    def get(self, request, id):
        subtopics_data = Subtopics.objects.filter(history_list=id)
        result_data = []

        for subtopic in subtopics_data:
            subtopic_dict = {
                'title': subtopic.title,
                'content': self.get_subtopic_content(subtopic)
            }
            result_data.append(subtopic_dict)

        loggerINFO.info(f'{datetime.now()} SubtopicWithContent {request.user.username}')
        return Response({'subtopics': result_data})

    def get_subtopic_content(self, subtopic):
        subtopic_content_data = SubtopicsContent.objects.filter(subtopics=subtopic)
        content_list = []

        for content in subtopic_content_data:
            content_dict = {
                'type': content.type,
                'text': content.text
            }
            content_list.append(content_dict)

        return content_list