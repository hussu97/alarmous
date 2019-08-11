from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Alarm(models.Model):
    """Model representing an alarm"""
    title = models.CharField(max_length=200, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    sound = models.ForeignKey('Sound', on_delete=models.CASCADE, default=1)
    time = models.DateTimeField()

    class Meta:
        ordering = ['time']
    
    def __str__(self):
        return f'{self.title} at {self.time}'
    def get_absolute_url(self):
        """Returns the url to access a detail record for this alarm."""
        return '/'


class Sound(models.Model):
    name = models.CharField(max_length = 200)
    audio = models.FileField()

    def __str__(self):
        return self.name