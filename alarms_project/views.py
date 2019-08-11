from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from alarms_project.models import Alarm
from django.contrib.auth.models import User
from alarms_project.forms import AlarmForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class HomePageView(LoginRequiredMixin,ListView):
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    model = Alarm
    context_object_name = 'alarm_list'
    paginate_by = 10
    template_name = 'home.html'

    def get_queryset(self):
        return Alarm.objects.filter(creator=self.request.user)

class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = "about.html"

class AlarmCreate(LoginRequiredMixin,CreateView):
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    model = Alarm
    form_class = AlarmForm
    def get_context_data(self, **kwargs):
        ctx = super(AlarmCreate, self).get_context_data(**kwargs)
        ctx['title'] = 'Add new alarm'
        return ctx
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(AlarmCreate, self).form_valid(form)

class AlarmUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    model = Alarm
    form_class = AlarmForm
    def get_context_data(self, **kwargs):
        ctx = super(AlarmUpdate, self).get_context_data(**kwargs)
        ctx['title'] = 'Update alarm'
        return ctx
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(AlarmUpdate, self).form_valid(form)

class AlarmDelete(LoginRequiredMixin,DeleteView):
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    model = Alarm
    success_url = '/'
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    model = User
    fields = ['first_name','last_name','username','email']
    def get_context_data(self, **kwargs):
        ctx = super(ProfileUpdate, self).get_context_data(**kwargs)
        ctx['title'] = 'Update Profile'
        return ctx