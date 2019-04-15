from django.urls import path
from practice.student import views

app_name = 'practice.student'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('browsejobs/', views.browsejobs, name='browsejobs'),
    path('showjob/<int:job_id>/', views.showjob, name='showjob'),
    path('information/<int:ent_id>/', views.information, name='information'),
    path('sendresume/<int:job_id>/', views.sendresume, name='sendresume'),
    path('applied/', views.applied, name='applied'),  #查看已投递简历
    path('protocol/', views.protocol, name='protocol'),
    path('internship/', views.internship, name='internship'),
    path('tripartite/', views.tripartite, name='tripartite'),
    path('employment/', views.employment, name='employment'),
    path('weeklyreport/', views.weeklyreport, name='weeklyreport'),
    path('reporthistory/', views.employment, name='reporthistory'),
]
