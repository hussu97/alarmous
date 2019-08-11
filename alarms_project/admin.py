from django.contrib import admin

# Register your models here.
from alarms_project.models import Alarm, Sound

admin.site.register(Alarm)
admin.site.register(Sound)