from django.db import models
import base64
from django.core.files.base import ContentFile

# Create your models here.
class Videos(models.Model):
    video = models.FileField(upload_to='videos', null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    golfclub = models.CharField(max_length=10, null=True)
    golfbaan = models.CharField(max_length=50, null=True)
    datum = models.DateTimeField(null=True)
    rpm = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    travel = models.IntegerField(null=True)
    angle = models.IntegerField(null=True)
    xas = models.IntegerField(null=True)
    airtime = models.IntegerField(null=True)
    simulatie = models.ImageField(null=True)

