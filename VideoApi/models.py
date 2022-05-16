from django.db import models

# Create your models here.
class Video(models.Model):
    video = models.FileField(upload_to='videos/videos/')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'