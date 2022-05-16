from typing_extensions import Self
from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from API.models import User, video, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


    def create(self, validated_data):
        """
        Create and return a new `video` instance, given the validated data.
        """
        return video.objects.create(**validated_data)

    def update(self, instance, validated_data, user):
        """
        Update and return an existing `video` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.GolfClub = validated_data.get('GolfClub', instance.GolfClub)
        instance.GolfCourse = validated_data.get('GolfCourse', instance.GolfCourse)
        instance.Id = validated_data.get('Id', instance.Id)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.video = validated_data.get('video', instance.video)
        # user = User(**validated_data, self)
        instance.save()
        return instance


