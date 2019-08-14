from django.db import models
from django.contrib.auth.models import User
from rules.contrib.models import RulesModel
import rules

@rules.predicate
def is_alarm_creator(user, alarm):
    return alarm.creator == user
rules.add_rule('can_edit_alarm',is_alarm_creator)
rules.add_perm('alarm.edit_alarm', is_alarm_creator)
# Create your models here.
class Alarm(RulesModel):
    """Model representing an alarm"""
    title = models.CharField(max_length=200, default = 'Alarm', help_text = 'Enter a nice name for the alarm')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    sound = models.ForeignKey('Sound', on_delete=models.CASCADE, default=1, help_text = 'Choose the sound for your alarm')
    time = models.DateTimeField(help_text = 'Choose a date and time for your alarm that is BEFORE the current time')

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