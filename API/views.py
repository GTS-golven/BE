from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from API.models import video
from API.serializers import APISerializer
from rest_framework.mixins import (CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet

# Create your views here.


@csrf_exempt
def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        video = video.objects.all()
        serializer = APISerializer(video, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def video_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        video = video.objects.get(pk=pk)
    except video.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = APISerializer(video)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = APISerializer(video, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        video.delete()
        return HttpResponse(status=204)

class APIViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 video
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many videos

      serializer_class = APISerializer
      queryset = video.objects.all()