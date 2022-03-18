from django.db import models

# Create your models here.

class Video(models.Model):
    name= models.CharField(max_length=100)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

def __str__(self):
    return self.name + ": " + str(self.videofile)

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    street_line_1 = models.CharField(max_length=255)
    street_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name
