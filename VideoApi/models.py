from django.db import models
import base64
from django.core.files.base import ContentFile

# Create your models here.
class Videos(models.Model):
    video = models.FileField()


