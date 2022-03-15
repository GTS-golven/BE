from django.db import models
from django.shortcuts import render
from .models import Video
from .forms import VideoForm

# Create your models here.

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

def __str__(self):
    return self.name + ": " + str(self.videofile)
