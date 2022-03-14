from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UsersSerializer
from rest_framework.permissions import AllowAny

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny, )