from django.db import models

# Create your models here.
class Login(models.Model):
    id = models.AutoField(
        primary_key=True
        )
    
    username = models.CharField(
        max_length=255,
        null=False
        )
    
    password = models.CharField(
        max_length=255,
        null=False
        )
    
class Meta:
    db_table = 'users'