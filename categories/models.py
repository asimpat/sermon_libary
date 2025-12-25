from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


# Create many-to-many relationship
# Add this to sermons/models.py
class Sermon(models.Model):
  
    categories = models.ManyToManyField('categories.Category', blank=True)