from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'main', views.HistoryViewSet)


urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += router.urls