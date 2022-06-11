from django.shortcuts import render
from . import models, serializers
from rest_framework import generics


# Create your views here.
class DataSetVideoView(generics.ListCreateAPIView):
    queryset = models.DataSetVideo.objects.all()
    serializer_class = serializers.DataSetVideoSerializer
