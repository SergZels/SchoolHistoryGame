from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'main', views.HistoryViewSet)
router.register(r'subtopics/(?P<id>\d+)', views.SubtopicsViewSet, basename='subtopics')
router.register(r'subtopicscontent/(?P<id>\d+)', views.SubtopicsContentViewSet, basename='subtopicscontent')
#router.register(r'subtopicsALL/', views.SubtContALL, basename='subtALL')
router.register(r'maincontent/(?P<id>\d+)', views.MainContentViewSet, basename='mainscontent')
urlpatterns = [
    path("", views.index, name="index"),
    path("load", views.load, name="load"),
    path("subtwithcontent/<str:id>", views.SubtopicWithContent.as_view(), name="subtwithcontent"),
]

urlpatterns += router.urls