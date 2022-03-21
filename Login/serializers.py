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
        
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user