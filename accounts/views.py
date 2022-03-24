from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render
from rest_framework import renderers
from . import serializers
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = (AllowAny, )

class UserGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = (AllowAny, )