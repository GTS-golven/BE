from rest_framework import serializers
from .models import Video
import os
import base64

class VideoSerializer(serializers.ModelSerializer):
    video = serializers.CharField()

    class Meta:
        model = Video
        fields = ('id', 'video')
        read_only_fields = ('id',)
