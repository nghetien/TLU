from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets
from django.http import JsonResponse
from news.models import Post
from news.serializers import FormAPI
from django.core import serializers

# Create your views here.

class TestAPI(APIView):
    def get(self,request,format=None):
        my_data = Post.objects.all()
        full_data = FormAPI(my_data,many = True)
        return Response(full_data.data)