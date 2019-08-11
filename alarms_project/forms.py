from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from alarms_project.models import Alarm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

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