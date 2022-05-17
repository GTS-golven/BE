from rest_framework import serializers
from .models import Video
import os

class VideoSerializer(serializers.ModelSerializer):
    video = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Video
        fields = ('id', 'video')
        read_only_fields = ('id',)
