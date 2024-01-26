from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoryList,Subtopics,SubtopicsContent,MainContent
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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