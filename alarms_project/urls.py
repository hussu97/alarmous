from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('signup/',views.signup, name = 'signup'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('profile/<int:pk>', views.ProfileUpdate.as_view(), name = 'profile'),
    path('alarm/create/', views.AlarmCreate.as_view(), name='alarm_create'),
    path('alarm/<int:pk>/update/', views.AlarmUpdate.as_view(), name='alarm_update'),
    path('alarm/<int:pk>/delete/', views.AlarmDelete.as_view(), name='alarm_delete'),
]