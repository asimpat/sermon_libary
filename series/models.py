from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='series/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-start_date']

    def __str__(self):
        return self.title
