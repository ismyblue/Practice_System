from django.urls import path
from practice.enterprise import views

app_name = 'practice.enterprise'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('postjobs/', views.postjobs, name='postjobs'),
    path('addjob/', views.addjob, name='addjob'),
    path('showjob/', views.showjob, name='showjob'),
    path('updatejob/', views.updatejob, name='updatejob'),
    path('deletejob/', views.deletejob, name='deletejob'),
    path('resumescreening/', views.resumescreening, name='resumescreening'),
    path('received/', views.received, name='received'),
    path('selected/', views.selected, name='selected'),
    path('internmanage/', views.internmanage, name='internmanage'),
]
