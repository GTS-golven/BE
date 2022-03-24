from django.db import models
from django.contrib.auth.models import AbstractUser

import os
from uuid import uuid4

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}-{}.{}'.format(instance.pk, uuid4().hex, ext)
            else:
                # set filename as random string
                filename = '{}-{}.{}'.format(id, uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper

    videofile= models.FileField(
        upload_to=path_and_rename('accounts/'), 
        null=True, 
        verbose_name="")

    def __str__(self):
        return self.username