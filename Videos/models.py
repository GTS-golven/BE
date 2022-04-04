from django.db import models
from django.db import models
from django.conf import settings
from typing_extensions import Required
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Videos(models.Model):
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    # Models for uploading videos
    video = models.FileField(upload_to=None, max_length=254)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    Id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    GolfClub = models.CharField(max_length=30, blank=True, default='')
    GolfCourse = models.CharField(max_length=30, blank=True, default='')
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']