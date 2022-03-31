from typing_extensions import Required
from rest_framework import serializers
from Videos.models import Videos, LANGUAGE_CHOICES, STYLE_CHOICES

class VideosSerializer(serializers.Serializer):
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    title = serializers.CharField(required=False, allow_blank=False, max_length=50)
    id = serializers.IntegerField(read_only=True)
    GolfClub = serializers.CharField(Required=False, allow_blank=False)
    GolfCourse = serializers.CharField(Required=True, allow_blank=True, max_length=50)
    date = serializers.DateTimeField(read_only=True)
    video = serializers.FileField(allow_empty_file=False)



 
    def create(self, validated_data):
        """
        Create and return a new `Videos` instance, given the validated data.
        """
        return Videos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Videos` instance, given the validated data.
        """
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.title = validated_data.get('title', instance.title)
        instance.id = validated_data.get('id', instance.id)
        instance.description = validated_data.get('description', instance.id)
        instance.date = validated_data.get('date', instance.date)
        instance.video = validated_data.get('video', instance.video)
        instance.GolfCourse = validated_data.get('GolfCourse', instance.GolfCourse)
        instance.GolfClub = validated_data.get('GolfClub', instance.GolfClub)
        instance.save()
        return instance