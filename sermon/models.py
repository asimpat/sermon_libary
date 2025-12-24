from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='sermons/audio/')
    speaker = models.ForeignKey(
        'Speaker', on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(
        'series.Series', on_delete=models.SET_NULL, null=True, blank=True)
    preached_date = models.DateField()
    duration = models.DurationField(null=True, blank=True)
    scripture_references = models.TextField(blank=True)
    view_count = models.IntegerField(default=0)
    download_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-preached_date']

    def __str__(self):
        return self.title


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)

    def __str__(self):
        return self.name
