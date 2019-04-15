from django.urls import path
from practice.student import views

app_name = 'practice.student'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('browsejobs/', views.browsejobs, name='browsejobs'),
    path('showjob/', views.showjob, name='showjob'),
    path('information/', views.information, name='information'),
    path('sendresume/', views.sendresume, name='sendresume'),
    path('applied/', views.applied, name='applied'),  #查看已投递简历
    path('protocol/', views.protocol, name='protocol'),
    path('internship/', views.internship, name='internship'),
    path('tripartite/', views.tripartite, name='tripartite'),
    path('employment/', views.employment, name='employment'),
    path('weeklyreport/', views.weeklyreport, name='weeklyreport'),
    path('reporthistory/', views.employment, name='reporthistory'),
]
