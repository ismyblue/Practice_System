from django.urls import path
from practice.teacher import views

app_name = 'practice.student'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('postmanage/', views.postmanage, name='postmanage'),
    path('browsejobs/', views.browsejobs, name='browsejobs'),
    path('applied/', views.applied, name='applied'),
    path('protocol/', views.protocol, name='protocol'),
    path('internship/', views.internship, name='internship'),
    path('tripartite/', views.tripartite, name='tripartite'),
    path('employment/', views.employment, name='employment'),
    path('weeklyreport/', views.weeklyreport, name='weeklyreport'),
    path('reporthistory/', views.employment, name='reporthistory'),
]
