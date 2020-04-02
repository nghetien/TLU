from django.urls import path
from .views import APIView
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api-view/',views.TestAPI.as_view()),
]