from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from alarms_project.models import Alarm
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ['title','sound','time']
    
    def __init__(self, *args, **kwargs):
        super(AlarmForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = DateTimePickerInput()
    def clean_time(self):
        my_time = self.cleaned_data['time']
        if my_time <= timezone.now():
            raise ValidationError(_(f'{my_time} is before current time, please modify alarm time'))
        return my_time

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']