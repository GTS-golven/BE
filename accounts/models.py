from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.deconstruct import deconstructible


import os
from uuid import uuid4

# Create your models here.

@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}-{}.{}'.format(instance.pk, uuid4().hex, ext)
        else:
            # set filename as random string
            filename = '{}-{}.{}'.format(id, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathRename("/accounts/")


class CustomUser(AbstractUser):
    # add additional fields in here

    videofile = models.FileField(
        upload_to=path_and_rename, 
        null=True, 
        verbose_name="")

    def __str__(self):
        return self.username