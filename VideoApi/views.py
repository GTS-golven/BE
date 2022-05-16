from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.

class VideoCreate(generics.CreateAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer