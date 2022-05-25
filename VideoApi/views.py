
from VideoApi.serializers import VideoSerializer
from rest_framework import viewsets
from .models import Videos


# Create your views here.
class VideosView(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer