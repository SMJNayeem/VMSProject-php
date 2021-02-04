from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice', views.notice, name='notice'),
    path('requisition', views.requisition, name='requisition'),
    path('chairman', views.forChairman, name='chairman'),
    path('user-cost', views.usercost, name='usercost'),
    path('profile', views.profile, name='profile'),
    path('profile/update-profile', views.updateprofile, name='updateprofile'),
]