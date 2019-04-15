from django.urls import path
from practice.teacher import views

app_name = 'practice.teacher'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('browsejobs/', views.browsejobs, name='browsejobs'),
    path('showjob/<int:job_id>/', views.showjob, name='showjob'),
    path('information/<int:ent_id>/', views.information, name='information'),
    path('studentmanage/', views.studentmanage, name='studentmanage'),
    path('browseweeklyreport/', views.browseweeklyreport, name='browseweeklyreport'),
    path('unread/', views.unread, name='unread'),
    path('readed/', views.readed, name='readed'),
]
