from rest_framework import serializers
from API.models import User, video, LANGUAGE_CHOICES, STYLE_CHOICES

class APISerializer(serializers.Serializer):
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    # video serializers
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Id = serializers.IntegerField(read_only=True)
    GolfClub = serializers.CharField()
    GolfCourse = serializers.CharField()
    description = serializers.CharField()
    video = serializers.FileField()
    date = serializers.DateTimeField()
    User = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and return a new `video` instance, given the validated data.
        """
        return video.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `video` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


