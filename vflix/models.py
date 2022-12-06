from django.db import models

class Video(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300, blank=False, null=False)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title