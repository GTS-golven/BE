# Generated by Django 4.0.3 on 2022-04-07 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_video_user_alter_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default=django.utils.timezone.now, max_length=254, upload_to=None),
            preserve_default=False,
        ),
    ]