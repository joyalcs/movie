from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
