from django.db import models
import base64
from django.core.files.base import ContentFile

# Create your models here.
class Videos(models.Model):
    video = models.FileField(upload_to='videos')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    golfclub = models.CharField(max_length=10, blank=True)
    golfbaan = models.CharField(max_length=50, blank=True)
    datum = models.DateTimeField()
    rpm = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    travel = models.IntegerField(blank=True)
    angle = models.IntegerField(blank=True)
    xas = models.IntegerField(blank=True)
    airtime = models.IntegerField(blank=True)
    simulatie = models.ImageField(blank=True)

