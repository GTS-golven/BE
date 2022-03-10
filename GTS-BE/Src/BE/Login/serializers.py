from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Login


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    def create(self, validated_data):
        owner = self.context['request'].user
        
        return Login.objects.create(
            owner = owner, 
            **validated_data
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the todo item instance in the database
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    class Meta:
        model = Login
        fields = (
            'id',
            'username',
            'password'
        )